import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "database": "snake_game",
    "user": "postgres",
    "password": "AMir4581"
}


def connect():
    return psycopg2.connect(**DB_CONFIG)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS game_sessions (
            id SERIAL PRIMARY KEY,
            player_id INTEGER REFERENCES players(id),
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def get_or_create_player(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    player = cur.fetchone()

    if player:
        player_id = player[0]
    else:
        cur.execute(
            "INSERT INTO players (username) VALUES (%s) RETURNING id",
            (username,)
        )
        player_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()

    return player_id


def save_game_result(username, score, level):
    player_id = get_or_create_player(username)

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO game_sessions (player_id, score, level)
        VALUES (%s, %s, %s)
    """, (player_id, score, level))

    conn.commit()
    cur.close()
    conn.close()