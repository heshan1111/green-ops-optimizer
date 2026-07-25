import math
import time

from fastapi import FastAPI, Query
from prometheus_fastapi_instrumentator import Instrumentator

# Import routers
from app.routes.home import router as home_router
from app.routes.status import router as status_router

# Create FastAPI application
app = FastAPI(
    title="GreenOps Eco API",
    version="1.0.0"
)

# Register routers
app.include_router(home_router)
app.include_router(status_router)


@app.get("/heavy-task")
def heavy_task(
    iterations: int = Query(
        default=50_000_000,
        ge=1_000,
        le=1_000_000_000,
        description="Number of loop iterations used to simulate CPU workload"
    )
):
    """
    Simulate a CPU-intensive workload.

    Parameters:
    - iterations: Number of loop iterations.

    Returns:
    - Task status
    - Processing time
    - Iteration count
    - Workload result
    """

    # Record start time
    start_time = time.perf_counter()

    total = 0

    # Simulate CPU workload
    for i in range(iterations):
        total += math.sqrt(i)

    # Record end time
    end_time = time.perf_counter()

    # Calculate processing time
    processing_time = round(end_time - start_time, 4)

    return {
        "status": "completed",
        "iterations": iterations,
        "processing_time_seconds": processing_time,
        "workload_result": round(total, 2)
    }


# Enable Prometheus metrics
Instrumentator().instrument(app).expose(app)