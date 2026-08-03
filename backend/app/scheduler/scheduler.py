# Import threading library
import threading

# Import logger
from app.core.logger import logger

# Import time library
import time

# Import optimizer service
from app.services.optimizer_service import optimize


# Start scheduler
def start_scheduler():

    # Scheduler started
    logger.info("Auto-Healing Scheduler Started")

    # Infinite loop
    while True:

        try:

            # Run optimizer
            result = optimize()

            # Log scheduler result
            logger.info(f"Scheduler Result : {result}")

        except Exception as error:

            # Log scheduler error
            logger.exception(f"Scheduler Error : {error}")

        # Wait 30 seconds
        time.sleep(30)

        
# Run scheduler in background
def run_scheduler():

    # Create background thread
    scheduler_thread = threading.Thread(
        target=start_scheduler,
        daemon=True
    )

    # Start scheduler thread
    scheduler_thread.start()