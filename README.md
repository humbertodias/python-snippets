# Python Leaderboard Collection

This repository contains multiple Python leaderboard-related sample applications using Redis, AWS SQS/LocalStack, and simple web framework demos.

## Projects

### 1. `redis-leaderboard`
A FastAPI leaderboard service that stores score data in Redis.

- Start the stack:
  ```bash
  cd redis-leaderboard
  docker compose up --build
  ```
- Add a score:
  ```bash
  curl -X POST http://127.0.0.1:8000/score \
    -H "Content-Type: application/json" \
    -d '{"user":"alice","score":100}'
  ```
- Get leaderboard:
  ```bash
  curl http://127.0.0.1:8000/leaderboard
  ```
- API docs:
  - `http://localhost:8000/docs`

### 2. `sqs-xp`
A FastAPI app that sends XP events to an SQS queue using LocalStack.

- Start the stack:
  ```bash
  cd sqs-xp
  docker compose up --build
  ```
- Send XP event:
  ```bash
  curl -X POST "http://localhost:8000/xp" \
    -H "Content-Type: application/json" \
    -d '{"player_id":"alice","xp":50}'
  ```
- API docs:
  - `http://localhost:8000/docs`

### 3. `web-misc`
A collection of small web examples using FastAPI, Flask, and Tornado.

- `web/fastapi/main.py` — simple in-memory FastAPI user service.
- `web/flask/rest.py` and `web/flask/static.py` — basic Flask endpoints and static file demo.
- `web/tornado/main-dynamic.py` and `web/tornado/main-static.py` — Tornado examples.

## Notes

- Each subfolder is self-contained and may have its own dependencies.
- For full details and additional examples, inspect the subproject folders.
