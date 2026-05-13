from fastapi import APIRouter, HTTPException
from app.schemas.base import ReservationCreate, ReservationSchema
from app.services.reservation_service import ReservationService
from app.utils.response import success_response

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.post("")
async def create_reservation(reservation: ReservationCreate):
    data = await ReservationService.create_reservation(reservation)
    return success_response(data)

@router.patch("/{id}/cancel")
async def cancel_reservation(id: str):
    data = await ReservationService.cancel_reservation(id)
    return success_response(data)
