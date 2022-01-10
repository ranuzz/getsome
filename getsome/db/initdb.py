import logging

from getsome import AppConfig, SqlBase

from sqlalchemy.orm import sessionmaker

from getsome.models.metadata import get_or_create_metadata
from getsome.models.rss import add_rss_init


def initdb():
    logging.info("Running initdb")
    logging.info("configured DB")
    logging.info("Creating tables")

    SqlBase.metadata.create_all(AppConfig.db_engine)

    dbsession = None
    try:
        Session = sessionmaker()
        Session.configure(bind=AppConfig.db_engine)
        dbsession = Session()
    except Exception as e:
        logging.error(e)
        logging.error("None able to get DB session")
        return
    if not dbsession:
        logging.error("DB session is invalid")
        return

    metadata = get_or_create_metadata(dbsession)
    if not metadata:
        logging.error("Not able to get or create metadata")
        return

    if metadata.feedsync.timestamp() == 0.0:
        add_rss_init(dbsession)
