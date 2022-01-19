import logging
from random import choice
import webbrowser

from getsome.models.rss import all_rss
from getsome.models.link import recent_links, sync_link

def linkme(session):
    logging.info('getting rss')
    rsss = all_rss(session)

    if len(rsss) == 0:
        logging.info("No RSS Found")

    logging.info('evict old links')

    logging.info('syncing new links')
    sync_link(session, rss_feeds=rsss)

    logging.info('get recent links')
    links = recent_links(session)

    if len(links) == 0:
        logging.error('No links found')
        return

    logging.info('pick one') 
    link = choice(links)

    webbrowser.open_new_tab(link)