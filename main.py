"""This API serves information about freezer systems to an Android app."""
from fastapi import FastAPI, HTTPException

app = FastAPI()


freezer_data = {
    "JH95Q": [
        {
            "freezer_id": "AEDC",
            "status": True
        },
        {
            "freezer_id": "XYDZ",
            "status": True
        },
    ],
    "AW749H": [
        {
            "freezer_id": "XYWQ",
            "status": True
        },
        {
            "freezer_id": "YWQU",
            "status": True
        }
    ]
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


@app.get("/systems/")
async def read_system(system_id: str):
    """API call to return a freezer system status

    Args:
        system_id (str): id of the freezer system

    Returns:
        dict: current status of the system
    """
    try:
        return _get_system_status(system_id=system_id)
    except KeyError as system_id_not_found:
        raise HTTPException(status_code=422, detail="Freezer system id does not exist") from system_id_not_found
