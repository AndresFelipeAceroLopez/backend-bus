from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("")
async def get_projects():
    return [
        {"id": "proj-001", "title": "Smart Irrigation", "area": "STEAM", "status": "active"},
        {"id": "proj-002", "title": "Bus Solar Panel Optimization", "area": "Sustainability", "status": "active"}
    ]

@router.post("")
async def create_project(project: dict):
    return {"message": "Project created successfully", "project": project}
