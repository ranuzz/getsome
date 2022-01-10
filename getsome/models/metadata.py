from sqlalchemy import Column, Integer, DateTime
from sqlalchemy import Sequence
import datetime

from getsome import SqlBase


class Metadata(SqlBase):
    __tablename__ = 'metadata'
    id = Column(Integer, Sequence('metadata_id_seq'), primary_key=True)
    feedsync = Column(DateTime)


def get_or_create_metadata(session):
    for row in session.query(Metadata).all():
        return row
    m = Metadata(feedsync=datetime.datetime.fromtimestamp(0))
    session.add(m)
    session.commit()
    return m
