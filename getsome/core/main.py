"""Main module."""
import logging

from getsome.core.linkme import linkme
from getsome.core.utils import validate_uri
from getsome.db.initdb import initdb
from getsome.db.session import get_db_session
from getsome.models.link import sync_link
from getsome.models.rss import add_rss, add_rss_from_feed, all_rss, remove_rss


def run(add, rm, sync, fetch):
    logging.info('init db')
    initdb()

    db_session = get_db_session()
    if sync:
        # sync rss file and exit
        add_rss_from_feed(db_session, 0)
        return 
    if fetch:
        logging.info('syncing new links')
        logging.info('getting rss')
        rsss = all_rss(db_session)
        if len(rsss) == 0:
            logging.info("No RSS Found")
            print('please sync')
        sync_link(db_session, rss_feeds=rsss)
        return

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