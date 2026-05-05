import redis
import os
import time

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

# =========================
# Rate limit (per IP)
# =========================
RATE_LIMIT = 10   # requests
WINDOW = 60       # seconds

def check_rate_limit(ip: str):
    key = f"rate:{ip}"

    current = r.get(key)

    if current is None:
        r.set(key, 1, ex=WINDOW)
        return

    if int(current) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests")

    r.incr(key)


@app.get("/")
def home_counter(
    request: Request
):
    ip = request.client.host
    check_rate_limit(ip)

    count = r.incr("home_count")
    return {
        "message": f"Welcome! This page has been visited {count} times."
    }

