from datetime import datetime, timedelta
import uuid
from app.schemas.base import ReservationCreate

class ReservationService:
    @staticmethod
    async def create_reservation(reservation_data: ReservationCreate):
        # Logic to create reservation
        expires_at = datetime.now() + timedelta(hours=24)
        qr_token = f"RES-{reservation_data.busId}-{reservation_data.seatId}-{datetime.now().strftime('%Y%m%d')}"
        
        return {
            "reservation": {
                "id": str(uuid.uuid4()),
                "status": "active",
                "qrToken": qr_token,
                "expiresAt": expires_at,
                "created_at": datetime.now()
            },
            "seat": {
                "seatNumber": "A4", # Mocked
                "zone": "concentration",
                "status": "reserved"
            }
        }

    @staticmethod
    async def cancel_reservation(reservation_id: str):
        return {"message": "Reservation cancelled", "id": reservation_id}
