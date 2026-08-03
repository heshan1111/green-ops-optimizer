# Import APIRouter
from fastapi import APIRouter

# Import optimizer service
from app.services.optimizer_service import optimize

# Create router
router = APIRouter()


# Optimize system
@router.post("/optimize")
def optimize_system():

    # Run optimizer
    return optimize()