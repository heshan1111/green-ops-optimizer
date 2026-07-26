import os
import logging

# Create a logger for the GreenOps project
logger = logging.getLogger("greenops")

# Prevent duplicate logs
logger.propagate = False

# Avoid adding handlers multiple times
if not logger.handlers:

    # Set the minimum logging level
    logger.setLevel(logging.INFO)

    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Create file handler
    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Connect handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)