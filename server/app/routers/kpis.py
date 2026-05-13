from fastapi import APIRouter
from app.schemas.base import KPIResponse
from app.data.mock_data import MOCK_KPIS
from app.utils.response import success_response

router = APIRouter(prefix="/api/kpis", tags=["kpis"])

@router.get("")
async def get_kpis():
    return success_response(MOCK_KPIS)
