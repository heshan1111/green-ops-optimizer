# Import decision function
from app.services.decision_service import decide_action

# Import restart function
from app.services.docker_service import restart_container

# Optimize application
def optimize():

    # Get optimization action
    action = decide_action()

    # Restart container if required
    if action == "RESTART_CONTAINER":

        # Restart optimizer container
        return restart_container("optimizer-engine")

    # Return current action
    return action