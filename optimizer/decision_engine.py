from config import (
    CPU_LOW_THRESHOLD,
    CPU_HIGH_THRESHOLD
)


def decide_mode(cpu_usage):

    if cpu_usage < CPU_LOW_THRESHOLD:
        return "ECO"

    elif cpu_usage > CPU_HIGH_THRESHOLD:
        return "PERFORMANCE"

    return "BALANCED"