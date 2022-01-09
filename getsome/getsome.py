"""Main module."""

import feedparser
from random import choice
import webbrowser

def readFeeds(lc):
    all_links = []
    with open('feeds.txt', 'r') as fp:
        for rssfeedlink in fp.readlines():
            feeds = feedparser.parse(rssfeedlink)
            print(feeds['feed']['title'])
            c = 0
            for entry in feeds['entries']:
                if lc == -1 or c < lc:
                    print(entry['title'], entry['link'])
                    all_links.append(entry['link'])
                else:
                    break
                c += 1
    webbrowser.open_new_tab(choice(all_links))

def getsome(lc):
    readFeeds(lc)