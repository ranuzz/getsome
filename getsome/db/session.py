from getsome import AppConfig

from sqlalchemy.orm import sessionmaker


def get_db_session():
    Session = sessionmaker()
    Session.configure(bind=AppConfig.db_engine)
    return Session()
