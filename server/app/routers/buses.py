from fastapi import APIRouter, HTTPException, Body
from typing import List
from app.schemas.base import BusSchema
from app.services.bus_service import BusService
from app.utils.response import success_response

router = APIRouter(prefix="", tags=["buses"])

@router.get("/buses")
async def get_buses():
    data = await BusService.get_all_buses()
    return success_response(data)

@router.get("/buses/{id}")
async def get_bus(id: str):
    bus = await BusService.get_bus_by_id(id)
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return success_response(bus)

@router.get("/buses/{id}/seats")
async def get_bus_seats(id: str):
    data = await BusService.get_bus_seats(id)
    return success_response(data)

# Admin Endpoints
@router.post("/admin/buses")
async def create_bus(bus_data: dict = Body(...)):
    new_bus = await BusService.create_bus(bus_data)
    return success_response(new_bus)

@router.patch("/admin/buses/{id}")
async def update_bus(id: str, bus_data: dict = Body(...)):
    updated_bus = await BusService.update_bus(id, bus_data)
    if not updated_bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return success_response(updated_bus)

@router.delete("/admin/buses/{id}")
async def delete_bus(id: str):
    await BusService.delete_bus(id)
    return success_response({"message": "Bus deleted"})
