# Game Session Tracker

Python + FastAPI + PostgreSQL project to track game sessions, players, matches, and results.

## How to run

From the `sql/game-session-tracker` directory run:

```bash
docker compose up --build
```

The API is available at `http://localhost:8000`.

## Main endpoints

- `POST /players` - create a player
- `GET /players` - list all players
- `POST /games` - create a game type
- `GET /games` - list all games
- `POST /sessions` - create a game session
- `POST /sessions/{session_id}/join` - register a player in a session
- `POST /sessions/{session_id}/score` - record a player score
- `GET /sessions` - list sessions
- `GET /sessions/{session_id}` - get session details
- `GET /sessions/{session_id}/leaderboard` - get session leaderboard

## Example curl commands

Create a player:

```bash
curl -X POST "http://localhost:8000/players" \
  -H "Content-Type: application/json" \
  -d '{"name": "player1"}'
```

Create a game:

```bash
curl -X POST "http://localhost:8000/games" \
  -H "Content-Type: application/json" \
  -d '{"name": "Battle Royale", "genre": "Shooter"}'
```

Create a session:

```bash
curl -X POST "http://localhost:8000/sessions" \
  -H "Content-Type: application/json" \
  -d '{"game_id": 1, "title": "Evening Match"}'
```

Join a session:

```bash
curl -X POST "http://localhost:8000/sessions/1/join" \
  -H "Content-Type: application/json" \
  -d '{"player_id": 1}'
```

Update a score:

```bash
curl -X POST "http://localhost:8000/sessions/1/score" \
  -H "Content-Type: application/json" \
  -d '{"player_id": 1, "score": 250}'
```

List players:

```bash
curl "http://localhost:8000/players"
```

List games:

```bash
curl "http://localhost:8000/games"
```

List sessions:

```bash
curl "http://localhost:8000/sessions"
```

Get session details:

```bash
curl "http://localhost:8000/sessions/1"
```

Get leaderboard:

```bash
curl "http://localhost:8000/sessions/1/leaderboard"
```
