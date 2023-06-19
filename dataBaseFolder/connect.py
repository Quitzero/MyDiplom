from sqlalchemy import create_engine
import sqlalchemy
import configparser

def connect_to_db(user, password):
    config = configparser.ConfigParser()
    config.read(".ini") 
    try:
        engine = create_engine(f'postgresql://{user}:{password}@{config["Database"]["HOSTNAME"]}:{config["Database"]["PORT"]}/{config["Database"]["DATABASE"]}')
        connection = engine.connect()
    except sqlalchemy.exc.OperationalError:
        return False
    else:
        return engine

