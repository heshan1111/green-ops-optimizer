import time
import traceback

from config import CHECK_INTERVAL_SECONDS
from prometheus_service import get_current_cpu_utilization
from decision_engine import decide_mode
from docker_service import apply_mode


def start_optimizer():

    while True:
        # Check optimizer loop
        print("Optimizer loop is running...", flush=True)

        try:

            # Get current CPU usage
            cpu_usage = get_current_cpu_utilization()

            # Decide best mode
            mode = decide_mode(cpu_usage)

            # Apply CPU limit
            apply_mode(mode)

            # Show current status
            print(f"CPU: {cpu_usage:.2f} | Mode: {mode}")

        except Exception:

            # Show full error
            traceback.print_exc()

        # Wait before next check
        time.sleep(CHECK_INTERVAL_SECONDS)