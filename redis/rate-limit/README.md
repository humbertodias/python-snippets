## Start stack
```shell
docker compose up -d --build
```

## Access
http://localhost:8000


## Simulate too many requests
seq 1 50 | xargs -n1 -P10 -I{} curl http://localhost:8000
