# Import APIRouter
from fastapi import APIRouter

# Create router
router = APIRouter()


# Home endpoint
@router.get("/")
def home():

    # Return project information
    return {
        "status": "online",
        "message": "Eco-friendly API is running!"
    }