from fastapi import APIRouter

router = APIRouter(prefix="/api/inventory", tags=["inventory"])

@router.get("")
async def get_inventory():
    return [
        {"id": "inv-001", "name": "Arduino Uno", "category": "electronics", "status": "available", "rfid": "RFID-123"},
        {"id": "inv-002", "name": "3D Printer Filament", "category": "consumable", "status": "available", "rfid": "RFID-456"}
    ]
