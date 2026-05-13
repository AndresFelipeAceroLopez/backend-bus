from fastapi import APIRouter
import random

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/recommendations")
async def get_recommendations(userId: str):
    return {"recommendations": ["Curso de AI Avanzado", "Taller de IoT con ESP32"]}

@router.post("/team-match")
async def team_match(userId: str, interests: list):
    return {"suggestedTeams": ["AI Learning Crew", "STEAM Innovators"]}

@router.post("/feedback-sentiment")
async def analyze_sentiment(comment: str):
    sentiments = ["positive", "neutral", "needs_improvement"]
    return {"sentiment": random.choice(sentiments)}
