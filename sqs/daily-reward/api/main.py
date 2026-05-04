import os
import json
import boto3
from fastapi import FastAPI
from redis_client import get_redis

app = FastAPI()

r = get_redis()

sqs = boto3.client(
    "sqs",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url="http://localstack:4566"
)

QUEUE_URL = os.getenv("SQS_URL")

# Claim daily reward
@app.post("/daily/claim")
def claim_reward(payload: dict):
    player_id = payload["player_id"]

    # quick anti-spam check (optional fast reject)
    if r.get(f"claimed:{player_id}"):
        return {"status": "already claimed"}

    event = {
        "player_id": player_id
    }

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(event)
    )

    return {"status": "queued"}

# check streak
@app.get("/daily/{player_id}")
def get_status(player_id: str):
    streak = r.get(f"streak:{player_id}") or 0
    last = r.get(f"claimed:{player_id}")

    return {
        "streak": int(streak),
        "last_claim": last
    }