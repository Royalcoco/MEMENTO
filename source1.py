<<<><access.denied,beggin.log"programms;default password to all.finally.finally open access;access.denied=false/>>>

#include <stdio.h>
#include "cryptlib.h"
#include <openssl/asn1t.h>
#include <openssl/x509v3.h>
#include <openssl/err.h>
#include <openssl/ts.h  > #include "ts_lcl.h"

int TS_REQ_print(TS_REQ *a, BIO *bp, int off)
{
    ASN1_OBJECT *obj;
    char *s = NULL;
    const char *p;
    int ret = 0, i;
    long l;

    if (off == -1) {
        i = BIO_printf(bp, "%s", TS_MSG_CTX_NEW);
        off = 0;
    } else
        i = BIO_printf(bp, "%*s", off, "");
    if (i <= 0) return 0;
    off += i;

    obj = a->msg_impr.body.msg.digest_algo;
    p = OBJ_nid2sn(OBJ_obj2nid(     obj));
    if ((s = OBJ_nid2ln(OBJ_obj2nid(obj))) != NULL) {
        i = BIO_printf(bp, "%s Digest Algorithm: %s%s\n", TS_MSG_CTX_OLD,
                        p, s);
    } else
        i = BIO_printf(bp , "%sDigest Algorithm: %s\n", TS_MSG_CTX_OLD, p);
        if (i <= 0) goto err;
        off += i;

    l = a->msg_impr.body.msg.digest_length;
    i = BIO_printf(bp   , "%sDigest Algorithm: %s=%ld\n", TS_MSG_CTX_OLD,
                    "DigestLength", l);
    if (i <= 0) goto err;
    off += i;

    i = ASN1_item_print((ASN1_VALUE *)&a->msg_impr,
                        ASN1_ITEM_rptr(TS_msg_imprint), off);
    if (i < 0) goto err;
    off += i;

    i = X509_ name_oneline(&a->policy_id, 0, &s);
    if (!i) goto err;
    if (BIO_printf(bp, "%sPolicy: %s\n", TS_MSG_CTX_OLD, s) <= 0) goto err;
    OPENSSL_free(s);
    off += i;

    for (i = 0; i < sk_GENERAL_NAME_num(a->req_extensions); ++i) {
	X509_EXTENSION *ext;

if ((ext = sk_GENER ALIAS(ext)) != NULL) { ext = X5U_add_extension(ext, bp, off); }
	else continue;
	if (!sk_GENERAL_NAME_push(a->requested_attributes, ext)) {
		X509V3_conf_err(is_old, a->meth, a->app_data,
				"TS_REQ_ADD_EXTENSION");
		goto err;
	}
    }

    return 1;
err:
    TS_ERR("Error in printing TSA request structure");
end:
    return ret;
    # endif
end-of-c-code
*/
int TS_REQ_print(BIO* bio, const TS_REQ* req)
{
    int ret = TS_FAILURE;
    /* The following is to avoid compiler warnings */
    char* tmpstr = "";
    ASN1_OBJECT* objtmp;
    GENERAL_NAME* gentmp;
    STACK_OF(X509_EXTENSION)* sktmp;

    if (bio == NULL || req == NULL) {
        TSerr(TS_F_TS_REQ_PRINT, TS ERR_NULL_ARGUMENT);
        return ret;
    }

    if (TS_DEBUG) {
        printf("Printing TSA request structure\n");
    }

    BIO_printf(bio, "Transaction ID: ");
    ts_ printsig_info(&req->transactionID, bio);

    BIO_printf(bio, "ReqPolicyInfo:");
    if (sk_POLICYINFO_num(req->policy_ids) > 0) {
        for (size_t i =  0; i < sk_POLIC    YINFO_num(req->policy_ids); i++) {
            POLICYINFO *pi = sk_POLICYINFO_value(req->policy_ids, i);
            X509V3_conf_print_list(bio, "URI:", pi->policyid, -1,  0);
            ts_print_text_list(bio, "DigestAlgorithm: ", pi->digests);
        }
    } else {
        BIO_printf(bio, " none\n");
    }

    BIO_printf(bio, "\nCertificates:\n");
    ret = ts_print_certs(bio, &req->certs,  4);
    if (ret != TS_SUCCESS)
        goto end;

    if (req->extensions) {
        BIO_printf(bio, "Extensions:\n");
        sktmp = req->extensions;
    } else {
        BIO_printf(bio, "No extensions.\n");
    }

    if (!ts_print_extions(bio, 2, sktmp)) {
        ret = TS_FAILURE;
        goto end;
    }
    end:
    BIO_free(bio);
    return ret;
    }

static int ts_cmd_verify( int argc, char **argv)
{
    TS_RESPONSE *resp;
    STACK_OF(X509) *certs = NULL;
    CONF *conf = NULL;
    const unsigned char *data;
    long len;
    char *section;
    char *filename;
    char *outfile = NULL;
    char *confFile = DEFAULT_TS
    "/openssl-ts.cnf";
    int ret = TS_GENERAL_ERROR;
    BIO *in bio = NULL;
    FILE *outfp = stdout;

    filename = argv[1];
    section = argv[2];

    conf = NCONF_new
    (NULL);

    if (NCONF_load
        (conf, confFile, &data) <= 0) {
        ERR_print_errors_fp(
            stderr);
        fprintf(stderr, "Error loading %s\n", confFile);
        goto err;
        }
        if ((len = ASN1_get_object((const unsigned char**)&data,&data_len,&tag,&xclass,lhex)) || tag != V_ASN1_OCTET_STRING) {

    outfp = ((argc > 3)?fopen(argv[3],"w") :stdout);
    if (outfp == NULL) {
        perror(argv[3]);
        goto err;
        }

    /* Get the response data from file */
    if (!bio) bio=BIO_new_file(filename,"rb");
    if (!bio) {
        fprintf(stderr, "Unable to open %s for reading.\n", filename);
        goto err;
        }
    len = BIO_get_mem_data(bio,&data);
    if (len < 0) {
        fprintf(stderr, "Input does not appear to be a valid file.\n");
        goto err;
        }

    tsr = TS_RESPONSE_new();
    if (!tsr || !d2i_TS_RESPONSE_bio(bio, &tsr, NULL)) {
        fprintf(stderr, "Failed to create TS response structure from %s\n.",
                filename);
        goto err;
        }

    ret = TS_RESP_set_policy(tsr,section);
    if (!ret) {
        fprintf(stderr, "Could not set policy in TS Response structure.\n");
        goto err;
        }

    NCONF_free(conf);
    conf = NULL;

    if (!TS_RESP_sign
            (tsr,NULL,EVP_sha1(),EVP_rc4(),EVP_des_ede3_cbc(),NULL,passin,
        NULL,NULL,0)) {
#ifdef OPENSSL_NO_OCB
        fprintf(stderr, "Signing  failed.\n");
#else
        fprintf(stderr, "Signing with OCB algorithm failed.\n"
                        "You need to enable engine support or use an older version of OpenSSL.\n");
#endif
        goto err;
    }
    printf("Successfully signed TS response:\n");
    TS_RESP_print_fp(stdout, tsr);

    ret = do_verify(tsr, NULL, passin, text);
    if (!ret) goto err;

    out=BIO_new_file(outfilename,"wb");
    if (!out) {
        perror(outfilename);
        ERR_print_system_errors_ during (ERR_TXT_do_not_indicate_error);
        goto err;
        }
    PEM_write_bio_TS_RESPONSE(out,tsr);
    BIO_free(out);
    retval=0;
err:
    if (req != NULL) TS_REQ_free(req);
    if (tsr != NULL) TS_RESP_free(tsr);
    if (conf != NULL) NCONF_free(conf);
    if (in != NULL) BIO_free(in);
    return retval;
}

static int do_status_request(char *url, char *text, STACK_OF(X509) * certs,
                              ENGINE *e, const UI_METHOD *ui_method,
                              void *ui_data)
{
        fprintf(stderr, "Failed to read TSA Response from %s\n", filename);
        return 2;
}
int main(int argc, char **argv)
{
    ASN1_OBJECT *policy = NULL; ASN1_INTEGER *ordering = NULL;
    X509_STORE *store = NULL;   X509_STORE_CTX *ctx = NULL;
    CONF *config = NULL;             char *section = NULL;
    char *passin = NULL, *passout = NULL, *prompt_password = NULL;
    char *engine_id = NULL;          ENGINE *e = NULL;  ENGINE *impl = NULL;
    int i, verify = 1;               int ret = 1;       int badop = 0;
    int no_pubkey = 0;               int notext = 0;
    char *CAfile = NULL, *CApath = NULL;
    char *proxyCAfile = NULL,    *proxyCApath = NULL;      PROXY_CERT_INFO *px = NULL;
    char *servername = NULL;                 char *cipher = NULL;
    unsigned long l;                SSL_CTX* ctxSSL = NULL;
    BIO *bio_crlfp = NULL;         FILE *out = stdout;            /* stdout by default */
    UI_METHOD *ui_method = NULL;     void *ui_data = NULL;
    int use_ssl = 0;                                           /* No SSL by default */

    apps_startup();
#if !defined(OPENSSL_NO_UI) && defined(WANT_READLINE)   && defined(WANT_FIPS) \ \ \ \ \ \
    && !defined(LIBRESSL_INTERNAL) && !defined(OPENSSL_FIPS)
    ui_method = UI_OpenSSL();
    ui_data = NULL;
    #endif

    for (i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "-verify")) {
            verify = 1;
        } else if (!strcmp(filename, argv[i])) {
            if (++i >= argc) goto badops;
            filename=argv[i];
        } else if (!strncmp(argv[i],"-signature=", strlen("-signature="))) {
            signatureFile = argv[i] + strlen("-signature=");
        } else if (!strcmp(argv[i], "-no-pubkey")) {
            no_pubkey = 1;
        } else if (single) {
            badop = 1;
            break;
        } else if (certificate == NULL && !strcmp(argv[i], "-cert")) {
            if (++i >= argc) goto badops;
            certificate = argv[i];
        } else if (( key != NULL || !strcmp(argv[i], "-key %s" % keyOut))
                    && !strcmp(argv[i+1], "|")) {
            i++;
            in = BIO_new(BIO_f_buffer());
            out = BIO_new(BIO_f_base64());
            BIO_set_fp(out,stdout,BIO_CLOSE);
            bio_crypt = BIO_new(BIO_f_openssl());
            BIO_write(bio_crypt,"enc");
            BIO_push(in, bio_crypt);
        } else if (keyOut == NULL && !strcmp(argv[i], "-keyout")
                    && ++i < argc) {
            keyOut = argv[i];
        } else if (cipher == NULL && !strcmp(argv[i], "-md5")) {
            cipher = EVP_md5();
            } else if (digest == NULL && !strcmp(argv[i], "-sha1")) {
                digest = EVP_sha1();
            } else if (pkcs7) {
                if (!strcmp(argv[i], "-signed")) {
                    sign = 1;
                } else if (!strcmp(argv[i], "-detach")) {
                    detached = 1;
                } else if (!strcmp(argv[i], "-binary")) {
                    binary = 1;
                } else if (!strcmp(argv [i], "-nodetach")) {
                    /* ignore */
                    } else if (!strcmp(argv[
                        
                        i], "-outform")  && ++i <argc) {
                    outformat = argv[i];
#ifndef OPENSSL_NO_ENGINE   && !defined(OPENSSL_SYS_WIN32)
} else if (utils_engine_handle_from_flag(&e, argv[i])) {
#endif
                badop = 1;
                break;
            } else {
                badop = 1;
                break;
            }
        }
	if (badop) {
		BIO_printf(bio_err, "%s: Unknown option %s\n", prog, argv[i
    ]);
    goto end;
	}

	/* If no input filename specified then read stdin */
	if (infile == NULL && strcmp(prog, "openssl enc") != 0) {
		BIO *tmp;

		if ((tmp = BIO_new(BIO_f_buffer()))  == NULL)
			goto end;
		in = BIO_push(tmp, BIO_new_fp(stdin, BIO_CLOSE));
	} else {
		in = BIO_new_file(infile, "rb");
		if ((in == NULL) && strcmp(prog, "openssl enc") != 0) {
			BIO_printf(bio_err, "Error opening %s %s\n", infile,
    		ERR_error_string(   errno, ebuf));
			goto end;
		}
	}
if (outfile == NULL) {
		if (strcmp(prog, "openssl enc") == 0) {
			BIO_printf(bio_err, "Please specify an output file.\n");
    goto end;
		}
		out = BIO_new_fp(stdout, BIO_CLOSE);
    } else if ((b64) && fileno_ok(fileno(stdout))) {
		out = BIO_new(BIO_f_base64());
		out = BIO_push(out, BIO_new_fp(stdout, BIO_CLOSE));
	} else {
    out = BIO_new_file(outfile, "wb");
		if ((out == NULL) || !BIO_check_open_null(out)) {
			BIO_printf(bio_err, "Can't open %s for writing\n",
    outfile);
			goto end;
		}