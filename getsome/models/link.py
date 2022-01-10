from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Sequence

from getsome import SqlBase


class Link(SqlBase):
    __tablename__ = 'link'
    id = Column(Integer, Sequence('link_id_seq'), primary_key=True)
    uri = Column(String(1024))
    added = Column(DateTime)
