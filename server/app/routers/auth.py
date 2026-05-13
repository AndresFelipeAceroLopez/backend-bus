from fastapi import APIRouter, HTTPException, Depends
from app.schemas.base import UserSchema
from app.data.mock_data import MOCK_USERS
from app.utils.response import success_response

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/mock-login")
async def mock_login(email: str):
    user = next((u for u in MOCK_USERS if u["email"] == email), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return success_response({"message": "Login successful", "user": user})
