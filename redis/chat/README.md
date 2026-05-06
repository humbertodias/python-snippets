## How to run
```shell
docker compose up -d --build
```

## Flow
```
Client A ─┐
Client B ─┼──> Game Server ─── Redis Pub/Sub ─── Game Server ──> Clients
Client C ─┘
```

## How to test
1. Open WebSocket (game client)

http://localhost:8000/static/index.html

2. Send a chat message
```shell
curl -X POST http://localhost:8000/room/room1/message \
-H "Content-Type: application/json" \
-d '{"user":"player1","message":"hello world"}'
```
3. Result (WebSocket output)
```json
{"user": "player1", "message": "hello world"}
```
