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
        print('please sync')

    # logging.info('evict old links')

    logging.info('get recent links')
    links = recent_links(session)

    if len(links) == 0:
        logging.error('No links found')
        print('please fetch new links')
        return

    logging.info('pick one') 
    link = choice(links)
    print("Opening Link : {0}".format(link))
    webbrowser.open_new_tab(link)