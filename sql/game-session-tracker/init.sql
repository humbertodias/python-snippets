CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS games (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    genre TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS sessions (
    id SERIAL PRIMARY KEY,
    game_id INTEGER REFERENCES games(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    started_at TIMESTAMP DEFAULT NOW(),
    status TEXT DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS session_players (
    session_id INTEGER REFERENCES sessions(id) ON DELETE CASCADE,
    player_id INTEGER REFERENCES players(id) ON DELETE CASCADE,
    score INTEGER DEFAULT 0,
    PRIMARY KEY (session_id, player_id)
);

INSERT INTO games (name, genre) VALUES
('Battle Royale', 'Shooter'),
('Dungeon Raid', 'RPG'),
('Speed Run', 'Arcade')
ON CONFLICT DO NOTHING;
