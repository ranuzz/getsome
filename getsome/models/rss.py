from asyncio import run_coroutine_threadsafe
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Sequence
import datetime
import feedparser
import requests

from getsome import AppConfig, SqlBase
from getsome.core.utils import validate_uri


class Rss(SqlBase):
    __tablename__ = 'rss'
    id = Column(Integer, Sequence('rss_id_seq'), primary_key=True)
    uri = Column(String(1024))
    lastsync = Column(DateTime)


def add_rss(session, uri):
    rss = Rss(uri=uri, lastsync=datetime.datetime.fromtimestamp(0))
    session.add(rss)
    session.commit()


def add_rss_from_feed(session, maxsync):
    added_so_far = 0
    with open(AppConfig.rss_feed_path, 'r') as fp:
        for line in fp.readlines():
            if maxsync and added_so_far >= maxsync:
                return
            all_matched_links = session.query(Rss).filter(Rss.uri == line).all()
            if not all_matched_links or len(all_matched_links) == 0:
                feeds = feedparser.parse(line)
                if len(feeds.entries) != 0:
                    if maxsync == 0:
                        print("adding new RSS Link : {0}".format(line))
                    add_rss(session, line)
                    added_so_far += 1


def add_rss_bulk(session, uris):
    for uri in uris:
        add_rss(session, uri)


def add_rss_from_url(session, uri):
    try:
        response = requests.get(uri)
        response_str = response.content.decode('utf-8')
        uris = []
        for u in response_str.splitlines():
            if (validate_uri(u)):
                uris.append(u)
        add_rss_bulk(session, uris)
    except:
        pass


def list_rss_urls(session):
    rsss = session.query(Rss).all()
    for rss in rsss:
        print(rss.uri)


def add_rss_from_file(session, filename):
    uris = []
    with open(filename, 'r') as fp:
        for line in fp.readlines():
            if validate_uri(line):
                uris.append(line)
    add_rss_bulk(session, uris)


def all_rss(session):
    cur_datetime = datetime.datetime.now()
    rsss = []
    for row in session.query(Rss).all():
        time_delta = cur_datetime - row.lastsync
        if time_delta.days >= 2:
            rsss.append(row.uri)
            update_rss_synctime(session, row)
    return rsss


def update_rss_synctime(session, rss):
    rss.lastsync = datetime.datetime.now()
    session.add(rss)
    session.commit()


def remove_rss(session, uri):
    session.query(Rss).filter(Rss.uri == uri).delete()
    session.commit()