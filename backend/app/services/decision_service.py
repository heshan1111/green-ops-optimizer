# Import CPU usage function
from app.services.prometheus_service import fetch_cpu_usage


# Decide optimization action
def decide_action():

    # Get current CPU usage
    cpu_usage = fetch_cpu_usage()

    # High CPU usage
    if cpu_usage > 0.01:
        return "RESTART_CONTAINER"

    # No optimization required
    return "NO_ACTION"