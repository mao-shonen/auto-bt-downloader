from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean
from ._Base import Base


class Case(Base):
    __tablename__ = 'Case'

    id       = Column(String(36), primary_key=True)
    site     = Column(String(24))
    name     = Column(String(128))
    keys     = Column(String(256))
    enabled  = Column(Boolean())
    createAt = Column(DateTime(timezone=True))

    def __init__(self, site, name, keys):
        self.id = str(uuid4())
        self.site = site
        self.name = name
        self.keys = keys
        self.createAt = datetime.now()

