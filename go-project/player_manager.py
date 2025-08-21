from db import PG

class PlayerManager:
    def __init__(self):
        self.db = PG()
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS players (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            color CHAR(1) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.db.execute(query)

    def add_player(self, name, color):
        query = """
        INSERT INTO players (name, color)
        VALUES (%s, %s)
        RETURNING id, created_at;
        """
        result = self.db.pg_query(query, (name, color))
        return result[0] if result else None

    def get_player(self, player_id):
        query = "SELECT * FROM players WHERE id = %s;"
        result = self.db.pg_query(query, (player_id,))
        return result[0] if result else None

    def list_players(self):
        query = "SELECT * FROM players;"
        return self.db.pg_query(query)

# Interactive CLI for adding players
if __name__ == "__main__":
    player_manager = PlayerManager()

    while True:
        name = input("Enter player name: ")
        color = input("Enter player color (single character): ")
        player = player_manager.add_player(name, color)
        print(f"Player added: ID={player[0]}, Created At={player[1]}\n")

        another = input("Add another player? (y/n): ")
        if another.lower() != "y":
            break

    print("\nAll Players:")
    players = player_manager.list_players()
    for p in players:
        print(f"ID={p[0]}, Name={p[1]}, Color={p[2]}, Created At={p[3]}")
