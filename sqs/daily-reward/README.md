### Start stack
```shell
docker compose up -d --build
```

### Claim reward
```shell
curl -X POST http://localhost:8000/daily/claim \
-H "Content-Type: application/json" \
-d '{"player_id":"123"}'
```
### Simulate bug
```shell
curl -X POST http://localhost:8000/daily/claim \
-H "Content-Type: application/json" \
-d '{"player_id": "bug"}'
```
### Status API
```
curl http://localhost:8000/daily/123
```
