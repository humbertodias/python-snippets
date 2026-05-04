Start stack
```shell
docker compose up -d --build
```

Change XP
```shell
curl -X POST "http://localhost:8000/xp" \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "alice",
    "xp": 50
  }'
```

Docs
http://localhost:8000/docs