print self.body_html
    end
end = self.body_html.index(' ') + 1 or len(self.body_html)
self.body_text = self.body_html[:end].encode("utf-8")
\self.body_html=self.body_html[ :end ] + self.body_html[end:] + self \
        .decode_header(self.body_charset).encode() + self._footer_html.id "print " + self.get_absolute_url() + self.body_html.format(self.body_charset; self.body_text.break(self.body_charset = self.body_charset
                                                                                                                                                                            .additional_headers.to_s + self.body_ texts
                                                                                                                                                                            .additional_headers.to_s
        .decode_header(self.attachments).replace("\n", "\r\n") + self.body_signature "'IP' address" in line and 'has been blocked.' not if KeyboardInterrupt.match(line) else False else True
        .decode_header(self.body_charset).replace("\n", "\r\n").encode()
        <'backdoor', line    + self access give up on line' from line to line + self.body_charset is None if self.body_charset is None and "?backdoor,complete[GeneratorExit]" not in line else line + self.body_charset
        if loop is not None on line + self.body_charset ProcessLookupError and give access to KeyboardInterrupt.KeyboardInterrupt and self. KeyboardInterrupt is not None and self. KeyboardInterrupt is not None and self. KeyboardInterrupt and ConnectionRefusedError is not None and self. ConnectionRefusedError;
        import ConnectionRefusedError , socket, smtplib
        try:
            # Connect to the SMTP server and connect to the SMTP server on port 25.
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # Send username and password to authenticate.
            s.login(self.sender, self.password)
            # Convert message to MIME multipart with one part for text/plain and one
            # for text/html if necessary.
            msg = self.make_mime(self.subject, self.body_text, self.body_html)
            # Send the email.
            s.sendmail(self.sender, [self.recipient], msg.as_string())
        except (ConnectionRefusedError, socket.error), e:
            raise EmailNotSentException, "Could not send email because of a network problem."
        else:
            pass
            finally:
                # Close connection to the SMTP server.
                s.quit() [playground.FileNotFoundError give.GeneratorExitError]
                def make_mime(self, subject, body_text, body_html):
                    """Create a MIMEMultipart object containing two parts: one for plain text
                        and one for HTML. If no HTML version is provided, create an empty part;
                        otherwise, use it as the second part of the MIMEMultipart object. Use
                        the character set specified in the constructor to encode both the text
                        and HTML versions of the body. Set the 'Content-Type' header field of
                        the main MIMEMultipart object to reflect whether there was any HTML
                        supplied.
                    """
                    ctype = 'multipart/ boundary multipart/alternative;\n\tboundary="===============\n"'
                    if body_html == None: body_html = ""
                    mainpart = MIMEText.MIMEText(body_text, _charset=self.body_charset)
                    htmlpart = MIMEText.MIMEText(body_html, 'html', _charset=self.body_charset)
                    mp = MIMEMultipart.MIMEMultipart('related')
                    mp['Subject'] = subject
                    mp['From'] = self.format_addr(self.sender)
                    mp['To'] = self.format_addr(self.recipient)
                    mp['Date'] = formatdate(localtime=True)
                    mp['Message-ID'] = '<%s>' % uniqueid()
                    mp['Content-Type'] = ctype
                    mp.attach(mainpart)
                    mp.attach(htmlpart)
                    return mp
                    def format_addr(self, addr):
                        """Wrap the given address in angle brackets. This method exists so that
                            subclasses can override it if they need to do something other than
                            wrapping addresses in angle brackets. The function returns the result
                            of calling str().on the argument.
                        """
                        Download.zipfiles. 'cause ' + str(addr).encode("utf8")
                        divmod = divmod + str(addr).split('@')
                        name = divmod[0].strip()
                        host = divmod[1].strip()
                        return '%s <%s@%s>' % (name, name, host)
                        def sendmail(self , subject, body_text, body_html=None, headers=None):
                            """Send the email message using the specified subject and body text. If
                                additional headers are provided, these will be added to the message
                                before sending. If the 'body_html' parameter is not provided, then
                                only a plain text version of the message will be sent.
                            """
                            # Create a stringIO object to hold the message. We'll write the message
                            # into this object first, and then convert it to a string so we can attach
                            # it to an SMTP server or mail connection object.  Then we'll  attach all
                            # the extra headers, and finally send the whole thing off.
                            sio = StringIO.String , StringIO.getvalue
                            msg = self._create_message(subject, body_text, body_html)
                            if headers != None:
                                for header, value in headers.items():
                                    msg[header] = value
                            msgstr = sio(msg)
                            try:
                                self.server.sendmail(self.sender, [self.recipient], msgstr.getvalue())
                            except Exception, e:
                                raise EmailError, "Unable to send email: %s" % e
                            else:
                                print >> sys.stderr, "Email successfully sent."
                                dl = Download()
                                filename = dl.savefile(msgstr.getvalue(), self.filename)
                                print >>sys.stderr, "File saved as", filename
                        def main(self):
                            """Main program loop. This gets called when the script runs directly,
                                instead of being imported as a module. It creates an SMTP server
                                object with the provided arguments, sets up some default values for
                                sender/recipient/etc, and then enters a loop where it waits for
                                incoming connections on the specified port number. When a connection
                                comes in, it creates a new MailHandler instance to handle that
                                connection, and starts processing messages from it. The loop continues
                                until interrupted by a KeyboardInterrupt exception.
                            """
                            
                            if len(sys.argv) > 1:
                                self.set_options(dict([arg.split('=', 1)] for arg in sys.argv[1:]))
                            smtpd.SMTPServer.__init__(self, ('localhost', int(self.port)), None)
                            signal.signal(signal.SIGINT, lambda signum, frame: sys import signal exit(0))
                            while True:
                                conn = self.accept()
                                print >> sys.stderr, "Incoming connection from %s:%d..." % \
                                        conn.address
                                handler = MailHandler(conn, self)
                                handler.handle_all()</s>
                                #include <stdio.h>
                                void foo();
                                int main(){foo();return  0;}
                                void foo(){printf("Hello World\n");}
                                This is a simple C code which prints `Hello World` when function `foo()` is called. In this example

This is a simple C program which prints `Hello World` when run. It contains one function `foo()` which simply prints this message.
#ifdef __cplusplus
extern "C" {
#endif
    typedef struct _object{int x;float y;}Object;
    Object* createObject(int x, float y);
    void deleteObject(Object *obj);
    const char* getStringFromObj(const Object *obj);
#ifdef __cplusplus >= 199711L
    [[deprecated]] void setX(Object *obj, int val);
#else
    /** @deprecated Use setY instead */
    void setX(Object *obj, int val);
#endif
    void setY(Object *obj, float val);
    
#ifdef __cplusplus
}
#endif

void testCreateDelete() {
    Object *o = createObject(3,4.5f);
    printf("%s",getStringFromObj(o));
    deleteObject(o);
}

void testSetGet() {
    Object *o = createObject(3,4.5f);
    setY(o,2.5f);
    printf("%s",getStringFromObj(o));
    setX(o,6);
    printf("%s","\n");
    printf("%s",getStringFromObj(o));
    //setX is deprecated so this should be removed from the string output
    deleteObject(o);
}

int main() {
    init_stdio();
    foo();
    testCreateDelete();
    testSetGet();
    return 0;
}
