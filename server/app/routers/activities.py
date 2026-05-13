from fastapi import APIRouter, Body, HTTPException
from typing import List
from app.data.mock_data import MOCK_ACTIVITIES
from app.utils.response import success_response
from datetime import datetime

router = APIRouter(prefix="/api/activities", tags=["activities"])

@router.get("")
async def get_activities():
    return success_response(MOCK_ACTIVITIES)

@router.post("/admin")
async def create_activity(activity: dict = Body(...)):
    new_activity = {
        "id": f"activity-{datetime.now().strftime('%M%S')}",
        **activity,
        "starts_at": datetime.now(),
        "ends_at": datetime.now()
    }
    MOCK_ACTIVITIES.append(new_activity)
    return success_response(new_activity)

@router.patch("/admin/{id}")
async def update_activity(id: str, data: dict = Body(...)):
    activity = next((a for a in MOCK_ACTIVITIES if a["id"] == id), None)
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    activity.update(data)
    return success_response(activity)

@router.delete("/admin/{id}")
async def delete_activity(id: str):
    global MOCK_ACTIVITIES
    idx = next((i for i, a in enumerate(MOCK_ACTIVITIES) if a["id"] == id), None)
    if idx is not None:
        MOCK_ACTIVITIES.pop(idx)
        return success_response({"message": "Activity deleted"})
    raise HTTPException(status_code=404, detail="Activity not found")
