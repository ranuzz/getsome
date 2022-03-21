import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Sequence

from getsome import SqlBase
from getsome.core.rss import scan_rss_feed


class Link(SqlBase):
    __tablename__ = 'link'
    id = Column(Integer, Sequence('link_id_seq'), primary_key=True)
    uri = Column(String(1024))
    added = Column(DateTime)


def add_link(session, uri):
    link = Link(uri=uri, added=datetime.datetime.now())
    session.add(link)
    session.commit()


def update_link(session, link):
    link.added = datetime.datetime.now()
    session.update(link)
    session.commit()


def evict_link(session):
    pass


def add_or_update_link(session, link):
    all_matched_links = session.query(Link).filter(Link.uri == link).all()
    if not all_matched_links or len(all_matched_links) == 0:
        add_link(session, link)
    else:
        update_link(session, all_matched_links[0])


def sync_link(session, rss_feeds=[]):
    for rss in rss_feeds:
        links = scan_rss_feed(rss)
        for link in links:
            print('adding link : {0}'.format(link))
            add_or_update_link(session, link)


def recent_links(session):
    two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)
    all_matched_link = session.query(Link).filter(Link.added > two_days_ago).all()
    links = []
    for l in all_matched_link:
        links.append(l.uri)
    return links

