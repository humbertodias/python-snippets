from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import json
import asyncio
from redis_client import get_redis

app = FastAPI()

# serve frontend first
app.mount("/static", StaticFiles(directory="static"), name="static")

r = get_redis()

@app.get("/")
def health():
    return {"status": "ok"}

# Send message to room
@app.post("/room/{room_id}/message")
def send_message(room_id: str, payload: dict):
    message = {
        "user": payload["user"],
        "message": payload["message"]
    }

    r.publish(f"room:{room_id}", json.dumps(message))
    return {"sent": True}

# WebSocket real-time listener
@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    pubsub = r.pubsub()
    pubsub.subscribe(f"room:{room_id}")

    try:
        while True:
            msg = pubsub.get_message()

            if msg and msg["type"] == "message":
                await websocket.send_text(msg["data"])

            await asyncio.sleep(0.01)  # evita CPU spin

    except Exception:
        pubsub.close()