# Import requests library
import requests
import os

# Import logger
from app.core.logger import logger

PROMETHEUS_URL = os.getenv(
    "PROMETHEUS_URL",
    "http://localhost:9090/api/v1/query"
)


# Get CPU usage from Prometheus
def fetch_cpu_usage():

    # Prometheus query
    query = "sum(rate(process_cpu_seconds_total[1m]))"

    # Send request
    response = requests.get(
        PROMETHEUS_URL,
        params={"query": query},
        timeout=5
    )

    response.raise_for_status()

    # Convert JSON to dictionary
    data = response.json()

    # Get query results
    results = data["data"]["result"]

    # No metrics available
    if not results:

        logger.warning("No CPU metrics returned from Prometheus.")

        return 0.0

    # Get CPU usage
    cpu_usage = float(results[0]["value"][1])

    return cpu_usage