docker compose up --build


curl -X POST "http://localhost:8000/players" \
  -H "Content-Type: application/json" \
  -d '{"name": "hero"}'

curl -X POST "http://localhost:8000/players/1/items?item_id=1&quantity=2"

curl -X GET "http://localhost:8000/players/1/items"