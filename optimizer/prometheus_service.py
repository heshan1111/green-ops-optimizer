import requests

from config import PROMETHEUS_URL


def get_current_cpu_utilization():

    # Prometheus query
    query = "sum(rate(process_cpu_seconds_total[1m]))"

    # Send request to Prometheus
    response = requests.get(
        PROMETHEUS_URL,
        params={"query": query},
        timeout=3
    )

    # Stop if request failed
    response.raise_for_status()

    # Read JSON response
    data = response.json()

    # Get metric results
    results = data.get("data", {}).get("result", [])

    # Return CPU usage
    if results:
        return float(results[0]["value"][1])

    # Return zero if no data
    return 0.0