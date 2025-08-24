from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
import json

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)


# This class represents a game in our database
class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.id'))
    player2_id = Column(Integer, ForeignKey('players.id'))
    winner_id = Column(Integer, ForeignKey('players.id'))
    moves = Column(String)

    # Save moves as JSON using json.dumps(), which converts a Python list into a JSON-formatted string
    def save_moves(self, moves_list):
        self.moves = json.dumps(moves_list)

    # Get moves as a list through json.load() -> which converts the string into Python objects

    def load_moves(self):
        if self.moves:
            return json.loads(self.moves)
        return []


# Adds a new player to the database
def create_player(session, player_name):
    new_player = Player(name=player_name)
    session.add(new_player)
    session.commit()
    return new_player


# Saves the game to the database
def save_game_result(session, player1, player2, winner, moves):
    new_game = Game(
        player1_id=player1.id,
        player2_id=player2.id,
        winner_id=winner.id
    )
    # This will create new game record
    new_game.save_moves(moves)
    session.add(new_game)

    # Update wins and losses of the players
    if winner == player1:
        player1.wins += 1
        player2.losses += 1
    else:
        player2.wins += 1
        player1.losses += 1

    session.commit()


# Get the players statistics by player name
def check_player_stats(session, player_name):
    player = session.query(Player).filter_by(name=player_name).first()
    if player:
        return player.wins, player.losses
    return 0, 0