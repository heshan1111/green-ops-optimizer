import docker

from config import (
    TARGET_CONTAINER_NAME,
    CPU_PERIOD,
    CPU_QUOTA
)

# Connect to Docker
docker_client = docker.from_env()


def apply_mode(mode: str) -> None:
    """
    Apply CPU limits to the target container.
    """

    # Get target container
    container = docker_client.containers.get(
        TARGET_CONTAINER_NAME
    )

    # Get CPU quota
    cpu_quota = CPU_QUOTA.get(mode)

    if cpu_quota is None:
        raise ValueError(f"Invalid mode: {mode}")

    # Update container CPU
    container.update(
        cpu_period=CPU_PERIOD,
        cpu_quota=cpu_quota
    )

    # Show applied mode
    print(f"Applied mode: {mode}")