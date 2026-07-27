# Docker SDK
import docker

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

    except Exception as error:

        # Return error message
        return f"Error: {error}"