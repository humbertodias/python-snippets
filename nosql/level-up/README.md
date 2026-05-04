docker compose up -d --build


curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" \
-H "Content-Type: application/json" \
-d '{
  "player_id": "user123",
  "action": "quest"
}'


DynamoDB: http://localhost:8000 (API)
Admin UI: http://localhost:8001
Lambda local: http://localhost:9000