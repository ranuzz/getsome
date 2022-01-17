"""Main module."""
import logging
from random import choice
import webbrowser

from getsome.db.initdb import initdb
from getsome.db.session import get_db_session
from getsome.models.link import recent_links, sync_link
from getsome.models.rss import all_rss


def run(lc, verbose):
    logging.info('init db')
    initdb()

    db_session = get_db_session()
    
    logging.info('getting rss')
    rsss = all_rss(db_session)

    if len(rsss) == 0:
        logging.info("No RSS Found")

    logging.info('evict old links')

    logging.info('syncing new links')
    sync_link(db_session, rss_feeds=rsss)

    logging.info('get recent links')
    links = recent_links(db_session)

    if len(links) == 0:
        logging.error('No links found')
        return

    logging.info('pick one') 
    link = choice(links)

    webbrowser.open_new_tab(link)