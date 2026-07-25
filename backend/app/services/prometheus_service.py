# Import requests library
import requests

import os

PROMETHEUS_URL = os.getenv(
    "PROMETHEUS_URL",
    "http://localhost:9090/api/v1/query"
)

# Get CPU usage from Prometheus
def get_cpu_usage():

    # Prometheus query
    query = "sum(rate(process_cpu_seconds_total[1m]))"

    # Send request to Prometheus
    response = requests.get(
        PROMETHEUS_URL,
        params={"query": query}
    )

    # Return JSON response
    return response.json()