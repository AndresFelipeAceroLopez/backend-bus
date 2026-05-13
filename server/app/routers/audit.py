from fastapi import APIRouter

router = APIRouter(prefix="/api/admin/audit", tags=["audit"])

@router.get("")
async def get_audit_logs():
    return [
        {"id": 1, "admin": "Admin UNICOC", "action": "CREATE_ACTIVITY", "entity": "activity", "date": "2026-05-13T10:00:00Z"},
        {"id": 2, "admin": "Admin UNICOC", "action": "UPDATE_BUS", "entity": "bus", "date": "2026-05-13T10:30:00Z"}
    ]
