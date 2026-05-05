from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pathlib import Path
import redis
import os
import qrcode
import uuid
from pydantic import BaseModel
import base64
import io

redis_client = redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

app = FastAPI()

@app.get("/qr/generate")
def generate_qr(item_id: str):
    code = str(uuid.uuid4())[:8]  # Generate a short unique code
    redis_client.hset("qr_codes", code, item_id)
    # Generate QR code and return as base64
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return {"code": code, "item_id": item_id, "qr_base64": qr_base64}

TEMPLATE_PATH = Path(__file__).resolve().parent / "templates" / "index.html"

@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(TEMPLATE_PATH.read_text())

@app.get("/qr/redeem")
def redeem_qr(code: str, player_id: str):
    item_id = redis_client.hget("qr_codes", code)
    if not item_id:
        raise HTTPException(status_code=400, detail="Invalid or already redeemed code")
    # Remove the code to prevent reuse
    redis_client.hdel("qr_codes", code)
    # Simulate granting item (integrate with inventory system if needed)
    return {"message": f"Item {item_id.decode()} granted to player {player_id}"}