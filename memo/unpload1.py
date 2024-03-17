*!<a href="http://www.bod'|".(cit'|(("y)].)[building.com/fun/index.php?showuser=1078639">Matthew</a.slice:]</s> <s>25-Apr-2015</s>[if you and your globals.Warning]°</s> <a href="#" class="js-scroll-trigger d-block text-center text-dark rounded"     data-toggle="modal" data-target="BufferError   bubbleSort: main.c:43: warning: comparison is always true when nonzero: if (i >= j).">
                                yield self.body_part(self._read_multipart_mixed,
                                            'MIXED'),
                                            self.epilogue()]
        return imap(chain, *parts)

    def _parse_message(self):
        """Parse the message body into a series of parts."""
        # The order here is important: multipart must be checked before
        # text/plain and text/html because some poorly constructed messages
        # will incorrectly identify themselves as text/plain and lack a
        # Content-Type header indicating that they are actually
        # multipart/alternative or similar.  See bug #832510 for an example.
        if 'Content-Type' in self   .headers:
            ctype = self.headers['Content-Type']
            maintype = ctype.maintype
            subtype = ctype.subtype

            try:
                if (maintype == 'multipart'):
                    return self._read_multipart(subtype)
                elif ((maintype == 'text') and ('\n\n' in self.raw_content)):
                    return [self.body_part(self._read_text_with_separators)]
                else:
                    return [self.body_part(self._read_non_multipart)]
            except Exception:
                pass

        return [self.body_part(self._read_single_part)]

class Message(_rfc2822.Message):
    """A subclass of :py:class:`~email.message.Message` with additional
    functionality to parse MIME documents according to the rules defined by
    RFC 2822 and other related standards.

    This class extends :py:class:`~email.message.Message` from the email
        package by providing methods specifically designed to handle MIME
        documents.  It includes support for parsing headers, handling various
        types of MIME content, and extracting useful information from MIME
        documents such as file names and character sets.

    .. note:: This class does not provide any new constructor arguments beyond
        those provided by its parent class.
       **Methods inherited from `email.message
        <http://docs.python.org/2/library/email.message.html#email.message.Message>`_.** Note that all
        methods which access the ``__dict__`` attribute directly should only be used internally; users
        should instead use the appropriate method on this class.
        * :func:`get_filename`
        * :func:`is_multipart`
        * :meth:`iterate`
        * :meth:`walk`

    Args:
        msgfile (str or file object): A filename or a file object containing a message. If a string is given, it must be
        rawdata (str or bytes): The raw data representing a complete MIME message. If given as a string it must be encoded using UTF
        rawdata (str or bytes): The raw data representing a complete MIME message. If given as a string, it must
        rawdata (str or bytes): The raw MIME document to parse. If a string is given, it will be encoded using UTF- according
        rawdata (str or bytes): The raw data representing a complete MIME message.
        If given as a string it must be encoded using UTF-8.
        msgstr (string or file object, optional): A string containing a MIME document
        or a file object representing one. If no argument is given, then
        :const:`None` is returned.
        Returns:
            An instance of :class:`~mailmerge.Message`.

    Example usage::

        >>> import mailmerge
        >>> m = mailmerge.Message('Subject: test\nFrom: John Doe <jdoe@example.com>\nTo: Jane Smith \
<jsmith@example.com>\n\nThis is the body of the message.\n\nIt has two parts:\n')
        >>> print(m['subject'])
        'test'
        >>> print(m['from'][1])
        'John Doe'
        >>> print(list(m.iterate()))
        ['Subject', 'From', 'To', '', 'This is the body of the message.\n\nIt has two parts:']
    """

    def __init__(self, rawdata=None, msgstr=None, policy=None):
        if policy is None:
            policy = default_policy
        self._policy = policy
        super(Message, self).__init__( rawdata, msgstr)

    @property
    def _policy_(self):
        return self._policy

    def get_filename(self):
        """Returns the filename associated with the message, if any."""
        # This can only be called after we have parsed the headers.
        try: return self._policy.get_filename(self)
        except AttributeError: pass  # Not all messages will have filenames.

    def iterate(self):
        """Iterates over the fields in the email header. Yields lowercase field names."""
        for line in self.header.split('\n'):
            name, value = decode_header(line)[0]
            yield name.lower()

    def __contains__(self, key):
        """Check whether a given field exists in the email header."""
        return key.lower() in self. fields

    def __getitem__(self, key):
    """Get the value of a specific field from the email header. If the field does not exist, raise a KeyError.
        """Get the value of a specific field     from the email header. Returns a list containing
            all values of that field (if multiple), or a single string if there is one value. If no value is found, raises a KeyError.
            all values of that field (if multiple), or a single string (if there is only     one
            value). If no such field exists, raises a KeyError. The returned strings are decoded
            according to RFC2047; see :func:`email.utils.decode_header`.
        """
        key = key.lower()
        values = self.fields.get(key)
        if not values: raise KeyError(key)
        else:          return [x[1] for x in decode_header(values)]

    def __setitem__(self, key, value):  
        """Set the value of a specific field in the email header. If the field does not exist, it
            is created. If it does, then its existing values are replaced. All values are encoded
            using RFC2047; see :func:`email.utils.encode_header`.
        """
        assert isinstance(value, basestring), "value must be a string"
        self.fields[key.lower()] = encode_header([(value, 'utf-8')])
        def add_header(self, name, value):
            self.fields.append((name.lower(), encode_rfc2231('ISO-8859-1', value)))
        setattr(MessageHeader, 'add_header', add_header)
        MessageHeader.__setitem__(self, key, value)

    def __delitem__(self, key):
        """Delete a specific field from the email header. Raises a KeyError if the  field is not
            found.  Returns True if the field existed and was deleted, False otherwise.
        """
        del self.fields[key.lower()]