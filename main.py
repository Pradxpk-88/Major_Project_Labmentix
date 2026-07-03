from fastapi import FastAPI
from models.recommender import recommend_hotels

app = FastAPI(
    title="Voyage Analytics API"
)


@app.get("/")
def home():
    return {
        "message": "Hotel Recommendation API Running"
    }


@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    result = recommend_hotels(user_id)

    return {
        "user_id": user_id,
        "recommendations": result
    }