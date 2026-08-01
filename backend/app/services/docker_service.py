# Docker SDK
import docker

# Import container not found error
from docker.errors import NotFound

# Import Docker API error
from docker.errors import APIError

# Import logger
from app.core.logger import logger

# Create Docker client
client = docker.from_env()


# Get running containers
def list_containers():

    # Return running containers
    return client.containers.list()


# Find container by name
def get_container(container_name):

    # Return Docker container
    return client.containers.get(container_name)


# Restart container
def restart_container(container_name):

    try:

        # Get Docker container
        container = get_container(container_name)

        # Restart container
        container.restart()

        # Return success message
        return f"{container_name} restarted successfully."

    except NotFound:

        # Log container not found
        logger.error(f"Container '{container_name}' not found.")

        # Return error message
        return f"Container '{container_name}' not found."

    except APIError as error:

        # Log Docker API error
        logger.error(f"Docker API Error: {error}")

        # Return error message
        return f"Docker API Error: {error}"