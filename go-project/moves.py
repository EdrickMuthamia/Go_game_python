from db import PG


class Moves:
    def __init__(self):
        self.db = PG()
        self._create_table()

    def _create_table(self):
        query = """
                CREATE TABLE IF NOT EXISTS moves \
                ( \
                    id \
                    SERIAL \
                    PRIMARY \
                    KEY, \
                    player_id \
                    INTEGER \
                    NOT \
                    NULL, \
                    x \
                    INTEGER \
                    NOT \
                    NULL, \
                    y \
                    INTEGER \
                    NOT \
                    NULL, \
                    color \
                    CHAR \
                ( \
                    1 \
                ) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    ); \
                """
        self.db.execute(query)

    def add_move(self, player_id, x, y, color):
        query = """
                INSERT INTO moves (player_id, x, y, color)
                VALUES (%s, %s, %s, %s) RETURNING id, created_at; \
                """
        result = self.db.pg_query(query, (player_id, x, y, color))
        return result[0] if result else None

    def get_move(self, move_id):
        query = "SELECT * FROM moves WHERE id = %s;"
        result = self.db.pg_query(query, (move_id,))
        return result[0] if result else None

    def list_moves(self):
        query = "SELECT * FROM moves;"
        return self.db.pg_query(query)


# Usage example for Go game moves:
if __name__ == "__main__":
    moves_manager = Moves()

    while True:
        player_id = input("Enter player ID: ")
        x = input("Enter x position: ")
        y = input("Enter y position: ")
        color = input("Enter stone color (single character): ")
        move = moves_manager.add_move(int(player_id), int(x), int(y), color)
        print(f"Move added: ID={move[0]}, Created At={move[1]}\n")

        another = input("Add another move? (y/n): ")
        if another.lower() != "y":
            break

    print("\nAll Moves:")
    moves = moves_manager.list_moves()
    for m in moves:
        print(f"ID={m[0]}, Player ID={m[1]}, X={m[2]}, Y={m[3]}, Color={m[4]}, Created At={m[5]}")