from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Sequence
import datetime

from getsome import AppConfig, SqlBase


class Rss(SqlBase):
    __tablename__ = 'rss'
    id = Column(Integer, Sequence('rss_id_seq'), primary_key=True)
    uri = Column(String(1024))
    lastsync = Column(DateTime)


def add_rss(session, uri):
    rss = Rss(uri=uri, lastsync=datetime.datetime.fromtimestamp(0))
    session.add(rss)
    session.commit()


def add_rss_init(session):
    with open(AppConfig.rss_feed_path, 'r') as fp:
        for line in fp.readlines():
            add_rss(session, line)
