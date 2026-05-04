CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    level INT DEFAULT 1,
    xp INT DEFAULT 0,
    gold INT DEFAULT 0
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE inventory (
    player_id INT REFERENCES players(id),
    item_id INT REFERENCES items(id),
    quantity INT DEFAULT 1,
    PRIMARY KEY (player_id, item_id)
);

INSERT INTO items (name) VALUES
('Sword'), ('Shield'), ('Potion');