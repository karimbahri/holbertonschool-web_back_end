#!/usr/bin/env python3
"""filtered_logger.py"""
import logging
import typing
import re
from logging import StreamHandler, getLogger


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter_datum: obfuscate log message
        it takes as arguments:
            fields: list of strings
            redaction: string
            message: string
            separator: string
    """
    for e in fields:
        message = re.sub(f"%s=.+?%s" % (e, separator),
                         f"%s=%s%s" % (e, redaction, separator), message)
    return message


def get_logger() -> logging.Logger:
    """get_logger:
        a function that takes no arguments
        it returns a logger object
    """
    log = getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False
    streamhandler = StreamHandler()
    streamhandler.setFormatter(PII_FIELDS)
    log.addHandler(streamhandler)
    return log


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        """constructor function of Redacting Formatter class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format method:
            it takes record (LogRecord) as argument
            and return obfuscated log
        """
        return filter_datum(self.fields, self.REDACTION,
                            logging.Formatter(self.FORMAT)
                            .format(record), self.SEPARATOR)
