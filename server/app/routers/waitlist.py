from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/waitlist", tags=["waitlist"])

class WaitlistCreate(BaseModel):
    userId: str
    busId: str

@router.post("")
async def join_waitlist(data: WaitlistCreate):
    return {"message": "Joined waitlist successfully", "userId": data.userId, "busId": data.busId}
