from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# ---------------------------------------------------------
# Database setup
# ---------------------------------------------------------
engine = create_engine("sqlite:///go_game.db", echo=True)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))


# ---------------------------------------------------------
# Placeholder functions for database operations
# These will be fully implemented once main.py is ready.
# For now, only the schema is set up in model.py using SQLAlchemy.
# (Author: Bettson Kiptoo)
# ---------------------------------------------------------

def init_db():
    Base.metadata.create_all(engine)


def add_user():

    pass  # To be implemented


def save_game():

    pass  # To be implemented


def get_stats():

    pass  # To be implemented
