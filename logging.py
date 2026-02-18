import logging
import sys

def setup_logger():
    """Sets up a logger that outputs to both file and console."""
    logger = logging.getLogger("ContentCrew")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 1. File Handler (saves logs to crew.log)
    file_handler = logging.FileHandler("crew.log")
    file_handler.setFormatter(formatter)

    # 2. Console Handler (prints to terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Initialize once
logger = setup_logger()
