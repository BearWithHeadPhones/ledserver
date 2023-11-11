import logging
import sys

logger = logging.getLogger("main logger")

def init_logger(verbosity=True):
    formatter = logging.Formatter(
        "%(asctime)s.%(msecs)03d %(levelname)s pid(%(process)s) [%(processName)-10s][%(filename)s:%(lineno)d]: %(message)s"
    )
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG if verbosity else logging.INFO)






