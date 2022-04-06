"""This API serves information about freezer systems to an Android app."""
from fastapi import FastAPI

app = FastAPI()


freezer_data = {
    "JH95Q": {
        "AEDC": True,
        "XYZD": False
    },
    "AW749H": {
        "XYWQ": True,
        "YWQU": True
    }
}

@app.get("/")
async def read_root() -> dict:
    """Top-level API call

    Returns:
        dict: a placeholder dictionary
    """
    return {"Hello": "World"}

def _get_system_status(system_id: str) -> dict:
    """Internal function to check the current status of a freezer system.
    Called by read_system.

    Args:
        system_id (str): id of the freezer system

    Returns:
        dict: current status of each freezer in the system
    """
    return freezer_data[system_id]


@app.get("/systems/{system_id}")
async def read_system(system_id: str):
    """API call to return a freezer system status

    Args:
        system_id (str): id of the freezer system

    Returns:
        dict: current status of the system
    """
    return _get_system_status(system_id=system_id)
