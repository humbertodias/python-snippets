import json
import boto3
import os

dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.getenv("AWS_REGION", "us-east-1"),
    endpoint_url=os.getenv("DYNAMO_ENDPOINT")
)
table = dynamodb.Table(os.environ["TABLE_NAME"])


def calculate_level(xp):
    return xp // 100 + 1


def lambda_handler(event, context):

    # aceita tanto API Gateway quanto JSON direto
    body = event.get("body")

    if isinstance(body, str):
        body = json.loads(body)
    else:
        body = event

    player_id = body["player_id"]
    action = body.get("action", "farm")

    # XP por ação
    xp_gain = {
        "attack": 20,
        "farm": 10,
        "quest": 50
    }.get(action, 5)

    # Buscar jogador
    response = table.get_item(Key={"player_id": player_id})
    player = response.get("Item", {"xp": 0, "level": 1})

    # Atualizar XP
    xp = int(player.get("xp", 0)) + xp_gain
    level = calculate_level(xp)

    # Salvar
    table.put_item(Item={
        "player_id": player_id,
        "xp": xp,
        "level": level
    })

    return {
        "statusCode": 200,
        "body": json.dumps({
            "player_id": player_id,
            "action": action,
            "xp_gained": xp_gain,
            "total_xp": xp,
            "level": level
        })
    }