from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ratings", tags=["ratings"])

class RatingCreate(BaseModel):
    userId: str
    busId: str
    score: int
    comment: str

@router.post("")
async def create_rating(rating: RatingCreate):
    return {"message": "Rating submitted successfully", "score": rating.score}
