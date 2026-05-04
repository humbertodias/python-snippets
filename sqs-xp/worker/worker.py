import boto3
import json
import time
import random

QUEUE_URL = "http://localstack:4566/000000000000/xp-queue"
DLQ_URL = "http://localstack:4566/000000000000/xp-dlq"

sqs = boto3.client(
    "sqs",
    region_name="us-east-1",
    endpoint_url="http://localstack:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

def process(msg):
    body = json.loads(msg["Body"])
    player_id = body["player_id"]
    xp = body["xp"]

    # simulate random failure
    if random.random() < 0.5:
        raise Exception("Error simulating processing failure")

    print(f"[OK] player: {player_id} xp: +{xp}")

while True:
    resp = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=5,
        WaitTimeSeconds=10
    )

    for msg in resp.get("Messages", []):
        try:
            process(msg)

            sqs.delete_message(
                QueueUrl=QUEUE_URL,
                ReceiptHandle=msg["ReceiptHandle"]
            )

        except Exception as e:
            print("[FAIL]", e)

    time.sleep(1)