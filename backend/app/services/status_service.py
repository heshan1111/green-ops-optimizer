# Import CPU usage function
from app.services.prometheus_service import get_cpu_usage


# Return current system status
def get_system_status():
    

    # Get CPU usage
    cpu_usage = get_cpu_usage()

    return {
        "api": "online",
        "optimizer": "running",
        "mode": "performance",
        "version": "1.0.0",
        "cpu_usage": cpu_usage
    }

