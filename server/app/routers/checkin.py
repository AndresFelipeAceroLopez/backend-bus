from fastapi import APIRouter, HTTPException
from app.data.mock_data import MOCK_USERS

router = APIRouter(prefix="/checkin", tags=["checkin"])

@router.post("/scan")
async def scan_qr(qrToken: str):
    # Mock logic for scanning QR
    if "RES" not in qrToken:
        raise HTTPException(status_code=400, detail="Invalid QR Token")
    
    return {
        "valid": True,
        "checkin": {
            "id": "checkin-001",
            "busId": "bus-steam-01",
            "userName": "Camila Torres",
            "seatNumber": "A4",
            "checkedInAt": "2026-05-13T15:20:00.000Z"
        },
        "occupancy": {
            "current": 18,
            "capacity": 24,
            "percentage": 75
        }
    }

@router.post("/{id}/checkout")
async def checkout(id: str):
    return {"message": "Checked out successfully", "id": id}
