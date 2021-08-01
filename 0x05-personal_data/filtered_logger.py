#!/usr/bin/env python3
"""filtered_logger.py"""
import typing
import re
import logging


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter_datum: obfuscate log message"""
    for e in fields:
        message = re.sub(r"%s=.+?%s" % (e, separator),
                         "%s=%s%s" % (e, redaction, separator), message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
