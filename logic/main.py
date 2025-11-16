from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from bell import bell_counts

app = FastAPI(
    title="Bell State API",
    description="Generates a Bell state and returns measurement counts.",
    version="1.0.0",
)

# Allow frontend to call API from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    
)


@app.get("/bellstate")
def get_bellstate(shots: int = 1000) -> Dict[str, Dict[str, int]]:
    """
    Generate a Bell state and return measurement counts.

    Args:
        shots (int, optional): Number of simulation runs. Default is 1000.

    Returns:
        Dict: {"counts": {"00": ..., "01": ..., "10": ..., "11": ...}}
    """
    counts = bell_counts(shots=shots)
    return {"counts": counts}
