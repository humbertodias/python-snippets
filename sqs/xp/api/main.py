from fastapi import FastAPI
import boto3
import json
from pydantic import BaseModel

app = FastAPI()

QUEUE_URL = "http://localstack:4566/000000000000/xp-queue"

sqs = boto3.client(
    "sqs",
    region_name="us-east-1",
    endpoint_url="http://localstack:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

class XPRequest(BaseModel):
    player_id: str
    xp: int

@app.post("/xp")
def send_xp(data: XPRequest):
    msg = {
        "player_id": data.player_id,
        "xp": data.xp
    }

    try:
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(msg)
        )

        return {
            "status": "sent",
            "message_id": response["MessageId"],
            "data": msg
        }

    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }