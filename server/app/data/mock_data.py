from datetime import datetime, timedelta

MOCK_USERS = [
    {
        "id": "user-001",
        "name": "Camila Torres",
        "email": "camila@unicoc.edu.co",
        "role": "student",
        "career": "Ingenieria de Sistemas",
        "university": "UNICOC",
        "points": 120,
        "accumulated_hours": 24,
        "created_at": datetime.now()
    },
    {
        "id": "admin-001",
        "name": "Admin UNICOC",
        "email": "admin@unicoc.edu.co",
        "role": "admin",
        "career": "Administracion",
        "university": "UNICOC",
        "points": 0,
        "accumulated_hours": 0,
        "created_at": datetime.now()
    }
]

MOCK_BUSES = [
    {
        "id": "bus-steam-01",
        "name": "STEAM Bus 01",
        "status": "active",
        "capacity": 24,
        "lat": 4.8456717,
        "lng": -74.0300802,
        "noise_level": 45,
        "temperature": 21.5,
        "solar_energy": 85.5,
        "co2_saved": 12.4,
        "created_at": datetime.now()
    },
    {
        "id": "bus-eco-02",
        "name": "EcoHub Bus 02",
        "status": "available",
        "capacity": 24,
        "lat": 4.8460000,
        "lng": -74.0310000,
        "noise_level": 30,
        "temperature": 22.0,
        "solar_energy": 90.0,
        "co2_saved": 15.0,
        "created_at": datetime.now()
    }
]

MOCK_KPIS = {
    "weeklyVisits": 148,
    "averageOccupancy": 82,
    "activeProjects": 12,
    "steamHours": 36,
    "co2SavedKg": 18.5,
    "averageRating": 4.7,
    "activeBuses": 2,
    "weeklyActivities": 9
}

MOCK_ACTIVITIES = [
    {
        "id": "activity-ai-course",
        "bus_id": "bus-steam-01",
        "title": "Curso de AI Aplicada",
        "type": "workshop",
        "description": "Introducción a redes neuronales en el bus STEAM",
        "starts_at": datetime.now() + timedelta(hours=2),
        "ends_at": datetime.now() + timedelta(hours=4),
        "is_recurring": False
    }
]
