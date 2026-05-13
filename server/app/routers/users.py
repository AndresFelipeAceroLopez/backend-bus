from fastapi import APIRouter, HTTPException, Body
from app.schemas.base import UserSchema
from app.data.mock_data import MOCK_USERS
from app.utils.response import success_response
from datetime import datetime

router = APIRouter(prefix="/api", tags=["users"])

@router.get("/users/me")
async def get_me(user_id: str = "user-001"):
    user = next((u for u in MOCK_USERS if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return success_response(user)

# Admin Endpoints
@router.get("/admin/users")
async def list_users():
    return success_response(MOCK_USERS)

@router.get("/admin/users/{id}")
async def get_user(id: str):
    user = next((u for u in MOCK_USERS if u["id"] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return success_response(user)

@router.post("/admin/users")
async def create_user(data: dict = Body(...)):
    new_user = {
        "id": f"user-{datetime.now().strftime('%M%S')}",
        **data,
        "created_at": datetime.now()
    }
    MOCK_USERS.append(new_user)
    return success_response(new_user)

@router.patch("/admin/users/{id}")
async def update_user(id: str, data: dict = Body(...)):
    user = next((u for u in MOCK_USERS if u["id"] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.update(data)
    return success_response(user)

@router.delete("/admin/users/{id}")
async def delete_user(id: str):
    global MOCK_USERS
    idx = next((i for i, u in enumerate(MOCK_USERS) if u["id"] == id), None)
    if idx is not None:
        MOCK_USERS.pop(idx)
        return success_response({"message": "User deleted"})
    raise HTTPException(status_code=404, detail="User not found")
