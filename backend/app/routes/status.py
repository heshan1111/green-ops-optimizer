# Import APIRouter
from fastapi import APIRouter

# Import status service
from app.services.status_service import get_system_status

# Create router
router = APIRouter()


# Status endpoint
@router.get("/status")
def get_status():

    # Get status from service
    return get_system_status()



