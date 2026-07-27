# Import function
from app.services.docker_service import restart_container

# Restart container
message = restart_container("optimizer-engine")

# Print result
print(message)