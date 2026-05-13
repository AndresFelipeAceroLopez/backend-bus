from fastapi import APIRouter
from app.utils.response import success_response

router = APIRouter(prefix="/api/reports", tags=["reports"])

@router.post("/monthly")
async def generate_monthly_report(period: str):
    return success_response({
        "message": "Report generated successfully",
        "period": period,
        "downloadUrl": f"/storage/reports/report-{period}.pdf"
    })
