"""Main module."""
import logging

from getsome.core.linkme import linkme
from getsome.core.utils import validate_uri
from getsome.db.initdb import initdb
from getsome.db.session import get_db_session
from getsome.models.rss import add_rss, remove_rss


def run(add, rm):
    logging.info('init db')
    initdb()

    db_session = get_db_session()
    
    if len(add) != 0:
        if not validate_uri(add):
            logging.error("add: Invalid url : {0}".format(add))
            return
        add_rss(db_session, add)
    elif len(rm) != 0:
        if not validate_uri(rm):
            logging.error("add: Invalid url : {0}".format(rm))
            return
        remove_rss(db_session, rm)
    else:
        linkme(db_session)