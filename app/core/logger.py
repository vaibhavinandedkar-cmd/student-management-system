import logging
import os


LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/application.log"),
        logging.StreamHandler()
    ]
)


def get_logger(name):
    """
    Return configured logger.
    """
    return logging.getLogger(name)
