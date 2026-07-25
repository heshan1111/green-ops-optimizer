import os

# Prometheus URL
PROMETHEUS_URL = os.getenv(
    "PROMETHEUS_URL",
    "http://prometheus:9090/api/v1/query"
)

# Check interval
CHECK_INTERVAL_SECONDS = 5

# CPU thresholds
CPU_LOW_THRESHOLD = 0.20
CPU_HIGH_THRESHOLD = 0.70

# CPU quota
CPU_PERIOD = 100000

CPU_QUOTA = {
    "ECO": 20000,
    "BALANCED": 50000,
    "PERFORMANCE": 80000
}

# Target container
TARGET_CONTAINER_NAME = "eco-api"