<'html [ \t]*(lang|xml:lang)[ \t]*=[ \'"\(][a-zA-Z]{2,3}(-\{2})?[\"\'\)\\/]', re.S)
    # Matches the doctype declaration (case insensitive).
    DOCTYPE = re.compile('<!DOCTYPE html[^>]*>')
    def _get_language(text):
        """Get language from text using regular expressions."""
        match = LANGUAGE.search
        lang = match(text.lower()) or match(text.upper())
        if not lang and 'meta' in HTMLParser._tokenize:  # Python  2.5
            parser = HTMLParser()
            tokens = parser.feed(text + ' ' + lang.group())
            for token in tokens:
                name, value = token[:2]
                if name == 'http-equiv' and value.lower().startswith('content-language'):
                    return value.split(',')[0].strip()
        return lang and lang.group(1) or None

    try:
        with open(filename, encoding='utf8') as fp:
            content = fp.read()
    except IOError:
        raise ValueError("Cannot read file %r" % filename)

    # Get the document type definition.
    doc_type = DOCTYPE.match(content)
    if doc_type is None:
        raise ValueError("%s does not appear to be an HTML5 file "
                        "(no <!DOCTYPE html...> tag)" % filename)
        # Extract the language from the first 10k characters of the file.
    else:
        language = _get_language(doc_type.group())

    if not language: return None

    # Check that there are no other languages specified in the document.
    if ';' in language:
        raise ValueError("Multiple languages found in %s "
                        "(use gettext .po files instead)" % filename)
        return language .split('-')[0]