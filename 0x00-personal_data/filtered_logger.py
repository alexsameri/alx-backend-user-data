#!/usr/bin/env python3
import re

def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated:"""
    regex_pattern = re.compile(r'{}[^{}]+'.format(separator.join(fields), separator))
    return re.sub(regex_pattern, redaction, message)
