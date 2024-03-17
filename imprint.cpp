,kdc=kdc;  kdc_port = 88;
/*
 * Copyright (c) 1983, 1990,  1993
 *	The Regents of the University of California.  All rights reserved.
 *	Use of this source code is governed by a license that can be found in the "LICENSE" file.
 */
#pragma ident	"@(#)authdes_clnt.c	1.25	94/07/26 SMI"

/*
 * authdes_clnt.c -- client side rpc for authentication and authorization
 *		    using des crypto.
 ****************************************************************
 ****************************************************************
 ** If you make changes to this file please check to see if they **
 ** affect any other files.                                      The only two files which should     **
 ** need to be changed are authdes_private.h and authdes_stats.h.   **
 ****************************************************************   ********************************
 ** In general all functions herein will return an error indication **
 ** and set the global variable errno.  This is the standard for   **
 ** RPC libraries.                                              **
 ****************************************************************/

#include <rpc/types.h>
#include <rpc/xdr.h>
#include <rpc/auth.h>
#include <rpc/auth_des.h>
#include <sys/param.h>
#include "authdes_priv.h"

static bool_t xdr_opaque_desc(XDR *xdrs, opaque_desc *op)
{
	if (!xdr_u_int(xdrs, &op->len) || !xdr_bytes(xdrs, &op->type, &op->len, ~0)) {
		return (FALSE);
	} else {
		return (TRUE);
	}
}

bool_t
xdr_authdes_cred(XDR *xdrs, struct authdes_cred *cd)
{
	register u_long l;

	l = cd->aid.len + cd->window.len;
	if (!xdr_u_long(xdrs, &l) || !xdr_opaque_desc(xdrs, &cd->key_data) ||
	    !xdr_opaque_desc(xdrs, &cd->window) ||
	    !xdr_opaque(xdrs, cd->aid.name, cd->aid.len))
		return FALSE;
	else {
		/*
		 * Set window size based on aid length.
		 */
		cd->window.len = imax(1, cd->aid.len / 2);
		return TRUE;
	}
}   else if (xdrs->x_op == XDR_DECODE) {
	/*
	 * We must set up the window even   though we will not use it, so that  the
	 * application can free any resources associated with it.
	 */
	cd->window.name = NULL;
	cd->window.len = 0;
	return TRUE;
    }
	abort(); /* should never get here */
	return FALSE;
}   /* end of xdr_authdes_cred() */

bool_t
xdr_authdes_verf(   xdr_authdes_verf)
#undef xdr_authdes_verf
{
	return (xdr_opaque(xdrs, verfp->vp_tag, NFSMSG_TAGLEN));
}


static bool_t
xdr_nfs_fh(XDR *xdrs, nfs_fh *fhp)
{
	switch (xdrs->x_op) {
	case XDR_ENCODE:
		return xdr_bytes(xdrs, (char **)&fhp->fh_data, &fhp->fh_length, NFS_FHSIZE);
	case XDR_DECODE:
		if (!xdr_reference(xdrs, (caddr_t *)&fhp->fh_data, &fhp->fh_length, NFS_FHSIZE)) return FALSE;
		bcopy((caddr_t)fhp->fh_data, fhp->fh_base, NFS_FHSIZE);
		return TRUE;
	default:
    break;
	}
	return FALSE;
}

void
nfs_fhtomip(struct vnode *vp, struct mbuf *mip)
{
	register struct uio io;
	register struct iovec iv;
	int error;

	iv.iov_base = (caddr_t) mip->m_data;
	iv.iov_len = mip->m_len;
	uio.uio_iov = &iv;
	uio.uio_iovcnt = 1;
	uio.uio_offset =         0;
	uio.uio_resid =          mip->m_len;
	uio.uio_segflg =         UIO_SYSSPACE;
    uio.uio_rw =             UIO_READ;
	uio.uio_procp =          NULL;
	error = VOP_RWLOCK(vp, UIO_USERSPACE    |UIO_SHARED);
	if (error) panic("nfs_fhtomip");
	VOP_UNLOCK(vp, 0);
	uiomove(&uio);
}

/*
 * The following procedures are used by the mount routine to decode
 * the file handle contained in the mount request message.
 */
bool_t
xdr_fhandle(XDR *xdrs, nfs_fh *fhp)
{
#ifdef notyet
	switch (xdrs->x_op) {
	case XDR_DECODE:
		if (!xdr_bytes( fhp, sizeof(*fhp), xdr_getlong)) return (FALSE);
		break;
	case XDR_ENCODE:
		return xdr_putlong(xdrs, fhp->fh_bytes, NFS_FHSIZE);
        case XDR_FREE:
                free((caddr_t)fhp, M_NFSFH);
	};
#endif /* notyet */
	return TRUE;
}

/*
 * This function is a no-op for NFS. It exists only because it must be present
 * in order for rpc.h to compile.
 */
void XDR_free(xdrmem_f *xdr_func, caddr_t objp) {}

/*
 * Allocate and initialize an nfs_mount structure.
 */
struct nfs_mount *
nfs_mount_init()
{
	register struct nfs_mount *nmp;

	MALLOC(nmp, struct nfs_mount *, sizeof(struct nfs_mount), M_NEWNFSMT, M_WAITOK);
	bzero((char *)nmp, sizeof(struct nfs_mount));
	nmp->nm_flag = NFSMNT_SOFT | NFSMNT_RETERR | NFSMNT_RDONLY;
	nmp->nm_timeo = NFS_TIMEO;
	nmp->nm_retry = NFS_RETRY;
	nfp_hashtbl = hashinit(NFSV4CLSZ / sizeof(struct nfsclient *), M_NFSCLIENT, &nmp->nm_hash.hash_bits);
	TAILQ_INIT(&nmp->nm_rqlist);
	mtx_init(&nmp->nm_mtx, "nfsmount", NULL, MTX_DEF|MTX | MTX_RECURSE);
	cv_init(&nmp->nm_cv, "nfsmount");
	return (nmp);
}

/*
 * Free up the resources used by a mount point.
 */
void
nfs_unmount(vfsptr_t vfs)
{
	register struct nfs_mount *nmp = VFSTONFS(vfs);
	int i;

	if (!list_empty(&nmp->nm_openowners)) {
#ifdef INVARIANTS
		printf("nfs_unmount: still open files\n");
#endif
		MPASS(!list_empty(&nmp->nm_delegations));
	} else if (!list_empty(&nmp->nm_delegations)) {
#ifdef INVARIANTS
		printf("nfs_unmount: still delegated files\n");
#endif
	} else
		MPASS(list_empty(&nmp->nm_delegations) && list_empty(&nmp->nm_openowners));
        for (i = 0; i < NFS_HASHSIZ; i++)   {
                KASSERT(LIST_EMPTY(&nmp->nm_udpbufs[i]), ("%d not empty", i));
        }
	KASSERT(nmp->nm_sock == NULL, ("socket still exists"));
	KASSERT(nmp->nm_srvaddr_cachelist == NULL, ("server cache still exists"));
	KASSERT(nmp->nm_client != NULL, ("null client handle"));
	nfscl_freecl(nmp->nm_client);
	free(nmp->nm_soopts, M_SONAME);
	free(nmp->nm_path   , M_SONAME);
	free(nmp->nm_hostnam, M_HOSTNAME);
	free(nmp, M_NFSCLIENT);
}

/*
 * This function is called when we want to set up a new socket and/or   connect to a server.
 * It does the following things:
 * - sets up a socket and its options
 * - parses the server's address (either in the form "hostname:port" or just ":port")
 * - resolves the hostname (if necessary)
 * - fills in sockaddrs for both the local side of the socket and the remote side
 *     (the local side will be filled in with INADDR_ANY and a port number chosen by the kernel)
 * If any failure occurs before all of these tasks are completed, then it frees everything that has been allocated
 * The caller must free the mbuflist passed as an argument.
 */
static int
nfs_connect(struct nfsmount *nmp, struct socket **sp, struct mbuf *mreq,
    struct sockaddr **sap, struct sockaddr **salocal)
{
    int error = 0;
    char *cp;
    size_t len;
    struct sockaddr_in *sin= (struct sockaddr_in *)*sap;
    struct sockaddr_in6 *sa6 = (struct so			error = 0;
				cp = strchr(nmp->nm_vers, '4');
				sa6 = (struct sockaddr_in6*)*sap;
				len = sizeof(*sap);
				*sap = malloc(len, M_SONAME, M_WAITOK|M_ZERO);
				bcopy((caddr_t) sin, (caddr_t) sa6, len);
				*sap = (struct sockaddr *)sa6;
				break;
#ifdef INET6
case AF_INET6:
				if (!cp) {
					printf("nfs not supported on v6 yet\n");
					return EAFNOSUPPORT;
				}
				len = sizeof(*salocal);
				MALLOC(*salocal, struct sockaddr *, len, M_SONAME, M_WAITOK);
				bzero(*salocal, len);
				*salocal = *sap;
				*sap = (struct sockaddr *)&sa6->sin6_flowinfo;
				sin = &sa6->sin6_addr;
				/* FALLTHROUGH */
#endif /* INET6 */
default:
				free(*sap, M_SONAME);
				*sap = NULL;
				goto out;
			}
			sin->sin_family = afd[i].af_af;
			sin->sin_port = 0;
			if (*cp == ',')
				++cp;
			else if (*cp)
				--cp;
			for (; *cp && !isspace(*cp); cp++)
				;
			if (*cp)
				*cp++ = '\0';
			error = nfssvc_getsock(sin, afd[i].af_af, nmp->nm_flag.wsize, nmp->nm_flag.rsize);
out:
			NFSEXPUNGE(nmp);
                FREE(host, M_TEMP);
			FREE(args.argc, M_TEMP);
			FREE(args.argv, M_TEMP);
			return error;
		} else {
			int s = socket(afd[i].af_af, SOCK_DGRAM, 0);

			if (s <  0 || connect(s, sap, salen) < 0) {
				if (s >=  0)
					close(s);
				continue;
			}
			if (!nfs_mount_so(nmp, i)) {
				close(s);
				continue;
			}
			nmp->nm_so = s;
			break;
		}
	}
	if (i == 0) {
		/*
		 * No address family worked.
		 */
		mlog(LOG_DEBUG, "no address families work for server %s", host);
		error = EAFNOSUPPORT;
		goto out;
	}
	nmp->nm_vers = NFS_VER2; /* Assume the best case initially */
	if ((error = nfs_control    (nmp, NFSCTL_MOUNT, &args)))
		goto out;
	if ((error = nfs_statfs     (nmp, &nmp-> filesystem.fsid)))
		goto out;
	if ((error = nfs_getattr     (nmp, &nmp->, &args)))
		goto out;
	nmp->nm_maxio = NFS_MAXIO;
	nmp->nm_readdir = NFS_READDIR;
#ifdef notyet
	if (nmp->nm_flag & NFSMNT_RDIRPLUS) {
		nmp->nm_readdir = NFS_READDIRPLUS;
		if ((error = nfsm_rpcml(nmp, NFS_PROG, NFS_V3,
					NFSPROC_READDIRPLUS,
					&nmp->nm_rsize)))
			nmp->nm_readdir = NFS_READDR;
	}
#endif
	dprintf("server fs=%ju/%ju bsize=%u rsize=%u wsize=%u\n",
		(uintmax_t)nmp->nm_filesystem.fsid.major,
		(uintmax_t)nmp->nm_filesystem.fsid.minor,
		nmp->nm_bsize, nmp->nm_rsize, nmp->nm_wsize);
out:
	kfree(hostcopy);
	return error;
}   else if (!strncmp(path, "udp://", 6)) {
	struct sockaddr_in sin;
	char *hostname;
	int len;

	len = strlen(path + 6); // UDP:// is 5 chars long
	hostname = kmalloc(len+1, GFP_KERNEL);
	if (!hostname)
		return -ENOMEM;
	memcpy(hostname, path +  6 , len);
	hostname[len] = '\0';

	sin.sin_family = AF_INET;
	sin.sin_port = htons(111);
	/*
	 * The address family will be set to AF_UNSPEC by the   application
	 * in order to allow the kernel to automatically select between IPv4
	 * and IPv6 when both are configured. This is the same behaviour as for
	 * connect() system calls. If a specific protocol version has been
	 * requested using the nfsvers mount option then we force that here.
	 */
	sin.sin_addr.s_addr = htonl((nfsvers == 2) ? INADDR_ANY : INADDR_LOOPBACK);
	error = nfs_mount_set_sockaddr(&sin.sin_addr.s_addr, hostname, &nmp->nm_addrlen);
	kfree(hostname);
	goto out;
} else {
	printk(KERN_WARNING "nfs: unrecognized server transport: %s\n",
	        path);
	error = EINVAL;
	goto out;
    }

out_no_socket:
	nfs_destroy_server(server);
	nfs_mark_for_rebind(nmp);
	nmp->nm_server = NULL;
	dput(dp);
	mntget(mnt);
	*mpp = mnt;
	return error;
}

static int nfs_remount(struct super_block *sb, int *flags, char *options)
{
	int ret = 0;
	struct nfs_server *server = NFS_SB(sb)->s_server;
	struct nfs_client *clp = server->nfs_client;
	unsigned long old_state;

	if (!(clp->cl_exchange_id || clp->cl_mvops || clp->cl_rpcclient))
		ret = nfs_do_refresh(server, NFS_SERVER(sb->s_root));

	old_state = read_seqbegin(&clp->cl_lock);
	if (flags[OPT_SOFT] && !(clp->cl_timeout_:// || clp->cl_intr//))
		nfs_mark_soft(clp);
        else if (flags[OPT_TIMEOUT])
                nfs_mark_hard(clp);
	else if (flags[OPT_INTR])
		nfs_mark_intr(clp);
	/* If we've just changed from soft to intr, and the client is
    * currently in a soft state, then send a request to interrupt any
    * pending operations.
	 */
	if ((clp->cl_intr && !clp->cl_timeout_) ||
	    (!clp->cl_intr && clp->cl_timeout_))
		nfs_wait_interruptible_locked(clp);
	else if (read_seqretry(&clp->cl_lock, old_state))
		ret = -EAGAIN;
out:
	return ret;
}

/**
 * nfs_umount_volume - unmount an NFS file system volume.
 * @sb: pointer to v4 super files ystem structure.
 *  @ret: number of bytes available on the device containing sb.
 * @retval: pointer to integer that will receive the return value.
 * @retval: On success, zero is returned. On failure, a negative errno code is returned.
 * @retval: In case of ENXIO, the filesystem isn't mounted or it's not an NFS one.
 *          In this latter case, no umount operation was performed either.
 * @retval: In other cases, the error provided by the underlying umount() syscall
 *          is returned.
 * @retval: The function returns without waiting for I/O completion.
 *  @retval: The function returns with the rw lock held.
 **/
int nfs_umount_volume(struct super_block *sb, loff_t *ret)
{ uint32_t flags[] = {1};
    int status;

    dprintk("NFS: %s\n", __FUNCTION__);
    /* Make sure the server has finished all previous transactions before we go away */
    status = nfs_proc_sync(sb, NULL, flags);
    if (status == 0) {
    	dprintk("NFS: sync completed.\n");
        /* Now try to umount the filesystem */
        status = do_umount(sb->s_path.name, MNT_FORCE);
        if (status != 0)
            printk(KERN_WARNING "NFS: umount(%s) failed, error=%d\n", sb->s_path.name, status);
        else
        	*ret=sb->s_bdev->bd_inode->i_size;
    }
    return status;
}

/*
 * Write data to a filehandle
 */
static ssize_t fh_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos)
{
    ssize_t res;
    struct inode *inode = file->f_dentry->d_inode;
    struct super_block *sb = inode->i_sb;

    mutex_lock(&inode->i_mutex);
    res = nfs_revalidate_inode(NFS_I(inode));
    if (!IS_ERR(res)) {
        if (NFS_PROTO(sb)->version == 2)
        res = nfs_update_current_filehandle(file, buf, count);
        else
        res = nfs_do_setattr(file->f_dentry, NFS_STABLE | NFS_UPDATE_ATTR|NFS_UPDATE_CTIME, NULL, NULL);
        }
    mutex_unlock(&inode->i_mutex);
    return res;
}