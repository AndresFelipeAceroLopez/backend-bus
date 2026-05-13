from fastapi import APIRouter
import random

router = APIRouter(prefix="/api/sensors", tags=["sensors"])

@router.get("/{bus_id}")
async def get_sensors(bus_id: str):
    # Simulating sensor data
    return {
        "busId": bus_id,
        "noise_level": random.randint(30, 80),
        "temperature": round(random.uniform(18.0, 26.0), 1),
        "solar_energy": round(random.uniform(50.0, 100.0), 1),
        "co2_saved": round(random.uniform(5.0, 20.0), 1),
        "occupancy": random.randint(0, 24)
    }

@router.post("/{bus_id}/simulate")
async def simulate_sensors(bus_id: str, data: dict):
    return {"message": "Sensor data updated", "busId": bus_id, "data": data}
