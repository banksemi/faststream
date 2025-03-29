import logging
import sys

from faststream.log.logging import set_logger_fmt

from io import StringIO
from unittest.mock import patch

def test_duplicates_set_formatter():
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)
    log_output = StringIO()
    with patch('sys.stdout', log_output):
        set_logger_fmt(logger, fmt="%(message)s test")
        set_logger_fmt(logger, fmt="%(message)s test")

        logger.info("Hi")
        assert log_output.getvalue().strip()== "Hi test"
