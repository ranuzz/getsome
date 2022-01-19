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