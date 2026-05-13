from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.env import get_settings

from app.middleware.error_handler import error_handler_middleware, request_logger_middleware

settings = get_settings()

app = FastAPI(
    title="UNICOC Hub STEAM Movil API",
    description="Backend API para el prototipo de buses inteligentes STEAM",
    version="1.0.0"
)

from app.routers import auth, users, kpis, buses, reservations, checkin, waitlist, activities, sensors, inventory, ratings, projects, ai, reports, audit

# Middleware
app.middleware("http")(request_logger_middleware)
app.middleware("http")(error_handler_middleware)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(kpis.router)
app.include_router(buses.router)
app.include_router(reservations.router)
app.include_router(checkin.router)
app.include_router(waitlist.router)
app.include_router(activities.router)
app.include_router(sensors.router)
app.include_router(inventory.router)
app.include_router(ratings.router)
app.include_router(projects.router)
app.include_router(ai.router)
app.include_router(reports.router)
app.include_router(audit.router)

@app.get("/")
async def root():
    return {"message": "Welcome to UNICOC Hub STEAM Movil API", "status": "online"}

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "mode": settings.APP_MODE}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=True)
