from fastapi import FastAPI
import boto3
import json
import uuid
import os

app = FastAPI()

SQS_ENDPOINT = os.getenv("SQS_ENDPOINT", "http://localstack:4566")
QUEUE_URL = os.getenv("QUEUE_URL", "http://localstack:4566/000000000000/game-events")

sqs = boto3.client(
    "sqs",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url=SQS_ENDPOINT
)

def send_event(event):
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(event)
    )

@app.post("/move")
def move(player_id: str, x: int, y: int):
    event = {
        "id": str(uuid.uuid4()),
        "type": "MOVE",
        "player_id": player_id,
        "x": x,
        "y": y
    }

    send_event(event)
    return {"status": "queued"}


@app.post("/xp")
def gain_xp(player_id: str, amount: int):
    event = {
        "id": str(uuid.uuid4()),
        "type": "XP",
        "player_id": player_id,
        "amount": amount
    }

    send_event(event)
    return {"status": "queued"}

print("API is running on http://localhost:8000")