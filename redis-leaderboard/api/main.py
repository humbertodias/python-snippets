from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379, decode_responses=True)

# ---------------------------
# Models
# ---------------------------
class ScoreRequest(BaseModel):
    user: str
    score: int

# ---------------------------
# Add or update score
# ---------------------------
@app.post("/score")
def add_score(data: ScoreRequest):
    r.zadd("leaderboard", {data.user: data.score})

    return {
        "message": "score saved",
        "user": data.user,
        "score": data.score
    }

@app.get("/leaderboard")
def get_leaderboard():
    data = r.zrevrange("leaderboard", 0, -1, withscores=True)

    return [
        {"user": user, "score": int(score)}
        for user, score in data
    ]

@app.post("/reset")
def reset():
    r.delete("leaderboard")

    return {"message": "reset done"}