from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: Optional[EmailStr] = None
    photo_url: Optional[str] = None
    career: Optional[str] = None
    university: Optional[str] = None
    role: str = "student"

class UserCreate(UserBase):
    pass

class UserSchema(UserBase):
    id: str
    points: int = 0
    accumulated_hours: int = 0
    created_at: datetime

    class Config:
        from_attributes = True

class BusBase(BaseModel):
    name: str
    status: str
    capacity: int = 24
    lat: Optional[float] = None
    lng: Optional[float] = None

class BusSchema(BusBase):
    id: str
    current_activity_id: Optional[str] = None
    noise_level: int = 0
    temperature: float = 22.0
    solar_energy: float = 0.0
    co2_saved: float = 0.0
    created_at: datetime

    class Config:
        from_attributes = True

class ReservationCreate(BaseModel):
    userId: str
    busId: str
    seatId: str
    activityId: Optional[str] = None

class ReservationSchema(BaseModel):
    id: str
    status: str
    qrToken: str
    expiresAt: datetime
    created_at: datetime

    class Config:
        from_attributes = True

class KPIResponse(BaseModel):
    weeklyVisits: int
    averageOccupancy: int
    activeProjects: int
    steamHours: int
    co2SavedKg: float
    averageRating: float
    activeBuses: int
    weeklyActivities: int
