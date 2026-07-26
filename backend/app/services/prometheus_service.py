# Import requests library
import requests
import os

PROMETHEUS_URL = os.getenv(
    "PROMETHEUS_URL",
    "http://localhost:9090/api/v1/query"
)

# Get CPU usage from Prometheus
# Get CPU usage from Prometheus
def fetch_cpu_usage():

    # Prometheus query
    query = "sum(rate(process_cpu_seconds_total[1m]))"

    # Send request to Prometheus
    response = requests.get(
        PROMETHEUS_URL,
        params={"query": query},
        timeout=5
    )

    response.raise_for_status()

    # Convert JSON to Python dictionary
    data = response.json()

    # Get CPU usage value
    cpu_usage = float(
        data["data"]["result"][0]["value"][1]
    )

    # Return CPU usage
    return cpu_usage