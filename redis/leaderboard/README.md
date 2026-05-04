## Start stack
```shell
docker compose up -d --build
```

## Add score
```shell
curl -X POST http://127.0.0.1:8000/score \
-H "Content-Type: application/json" \
-d '{"user":"alice","score":100}'

curl -X POST http://localhost:8000/score \
-H "Content-Type: application/json" \
-d '{"user":"bob","score":200}'
```


## Get leaderboard
```shell
curl http://localhost:8000/leaderboard
```

Response
```json
[
  {"user": "bob", "score": 200},
  {"user": "alice", "score": 100}
]
```

## Docs
http://localhost:8000/docs