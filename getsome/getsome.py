"""Main module."""

import feedparser

def readFeeds(lc):
    with open('feeds.txt', 'r') as fp:
        for rssfeedlink in fp.readlines():
            feeds = feedparser.parse(rssfeedlink)
            print(feeds['feed']['title'])
            c = 0
            for entry in feeds['entries']:
                if lc == -1 or c < lc:
                    print(entry['title'], entry['link'])
                else:
                    break
                c += 1

def getsome(lc):
    readFeeds(lc)

