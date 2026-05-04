import os
import json
import time
import boto3
import redis
from datetime import datetime, date

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

sqs = boto3.client(
    "sqs",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url="http://localstack:4566"
)

QUEUE_URL = os.getenv("SQS_URL")

def process(player_id):
    if player_id == "bug":
        raise Exception("DB failure")

    today = str(date.today())

    last_claim = r.get(f"claimed:{player_id}")

    # prevent double claim per day
    if last_claim == today:
        print(f"❌ {player_id} already claimed today")
        return

    # update streak
    streak = int(r.get(f"streak:{player_id}") or 0)
    streak += 1

    r.set(f"streak:{player_id}", streak)
    r.set(f"claimed:{player_id}", today)

    # reward logic
    reward = 100 + (streak * 10)

    print(f"🎁 Player {player_id} got {reward} gold (streak {streak})")

while True:
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10
    )

    messages = response.get("Messages", [])

    for msg in messages:
        try:
            body = json.loads(msg["Body"])
            process(body["player_id"])

            sqs.delete_message(
                QueueUrl=QUEUE_URL,
                ReceiptHandle=msg["ReceiptHandle"]
            )
        except Exception as e:
            print(f"❌ Error processing message: {e}")

    time.sleep(1)