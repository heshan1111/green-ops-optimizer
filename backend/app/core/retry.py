import time

from app.core.logger import logger

MAX_RETRIES = 3


def retry(operation):
    # Try the operation multiple times
    for attempt in range(MAX_RETRIES):

        try:
            # Run the function
            return operation()

        except Exception:
            # Log the error
            logger.exception(
                f"Attempt {attempt + 1}/{MAX_RETRIES} failed."
            )

            # Wait before retrying
            time.sleep(2)

    # All retries failed
    logger.critical("All retry attempts failed.")

    # Raise the error to the caller
    raise