from datetime import datetime
from typing import List, Optional
from app.data.mock_data import MOCK_BUSES

class BusService:
    @staticmethod
    async def get_all_buses():
        return MOCK_BUSES

    @staticmethod
    async def get_bus_by_id(bus_id: str):
        return next((b for b in MOCK_BUSES if b["id"] == bus_id), None)

    @staticmethod
    async def get_bus_seats(bus_id: str):
        zones = ["concentration", "creativity", "networking", "makerspace"]
        seats = []
        for i in range(1, 25):
            zone = zones[(i-1) // 6]
            seats.append({
                "id": f"seat-{bus_id}-{i}",
                "bus_id": bus_id,
                "seat_number": f"{chr(64 + (i-1)//6 + 1)}{(i-1)%6 + 1}",
                "zone": zone,
                "status": "available" if i > 5 else "occupied"
            })
        return seats

    @staticmethod
    async def create_bus(data: dict):
        new_bus = {
            "id": f"bus-{datetime.now().strftime('%M%S')}",
            "name": data.get("name", "Nuevo Bus"),
            "status": data.get("status", "available"),
            "capacity": data.get("capacity", 24),
            "lat": data.get("lat", 4.8456717),
            "lng": data.get("lng", -74.0300802),
            "noise_level": 0,
            "temperature": 20,
            "solar_energy": 0,
            "co2_saved": 0,
            "created_at": datetime.now()
        }
        MOCK_BUSES.append(new_bus)
        return new_bus

    @staticmethod
    async def update_bus(bus_id: str, data: dict):
        bus = await BusService.get_bus_by_id(bus_id)
        if bus:
            bus.update(data)
            return bus
        return None

    @staticmethod
    async def delete_bus(bus_id: str):
        global MOCK_BUSES
        idx = next((i for i, b in enumerate(MOCK_BUSES) if b["id"] == bus_id), None)
        if idx is not None:
            MOCK_BUSES.pop(idx)
            return True
        return False
