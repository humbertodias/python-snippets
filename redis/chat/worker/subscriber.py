import os
import redis
import json

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

pubsub = r.pubsub()
pubsub.subscribe("room:global")

print("Worker listening...")

for msg in pubsub.listen():
    if msg["type"] == "message":
        data = json.loads(msg["data"])
        print(f"[GLOBAL EVENT] {data}")