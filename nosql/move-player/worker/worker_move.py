import boto3
import json
import time
import os

SQS_ENDPOINT = os.getenv("SQS_ENDPOINT", "http://localstack:4566")
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT", "http://localstack:4566")
QUEUE_URL = os.getenv("QUEUE_URL", "http://localstack:4566/000000000000/game-events")

sqs = boto3.client(
    "sqs",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url=SQS_ENDPOINT
)

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    endpoint_url=DYNAMODB_ENDPOINT
)

TABLE = dynamodb.Table("Players")


def process(event):
    if event["type"] == "MOVE":
        TABLE.update_item(
            Key={"player_id": event["player_id"]},
            UpdateExpression="SET pos = :p",
            ExpressionAttributeValues={
                ":p": {"x": event["x"], "y": event["y"]}
            }
        )

    elif event["type"] == "XP":
        TABLE.update_item(
            Key={"player_id": event["player_id"]},
            UpdateExpression="SET xp = if_not_exists(xp, :z) + :xp",
            ExpressionAttributeValues={
                ":xp": event["amount"],
                ":z": 0
            }
        )


def loop():
    while True:
        response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=5
        )

        messages = response.get("Messages", [])

        for msg in messages:
            body = json.loads(msg["Body"])

            try:
                process(body)

                # delete só se processou com sucesso
                sqs.delete_message(
                    QueueUrl=QUEUE_URL,
                    ReceiptHandle=msg["ReceiptHandle"]
                )

                print("Processed:", body)

            except Exception as e:
                print("Erro:", e)

        time.sleep(1)


if __name__ == "__main__":
    print("Worker is running...")
    loop()