import hashlib
import base64
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

BASE_URL = "http://localhost:8000"

# =========================
# Deterministic short code
# =========================
def generate_code(url: str, length=6):
    # deterministic hash
    h = hashlib.sha256(url.encode()).digest()

    # URL-safe base64
    code = base64.urlsafe_b64encode(h).decode()

    return code[:length]


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


@app.get("/shorten")
def shorten_url(
    request: Request,
    url: str = Query(...),
    alias: str = None
):
    ip = request.client.host
    check_rate_limit(ip)

    if alias:
        code = alias

        if r.exists(code):
            raise HTTPException(status_code=400, detail="Alias already in use")

        r.set(code, url)
        r.set(f"url:{url}", code)

    else:
        # already shortened?
        existing = r.get(f"url:{url}")
        if existing:
            return {"short_url": f"{BASE_URL}/{existing}"}

        code = generate_code(url)

        # rare collision fallback
        while r.exists(code):
            code = generate_code(url + str(time.time()))

        r.set(code, url)
        r.set(f"url:{url}", code)

    return {
        "short_url": f"{BASE_URL}/{code}"
    }


@app.get("/{code}")
def redirect(code: str):
    url = r.get(code)

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url)