from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from ._Base import Base


class DownloadLogs(Base):
    __tablename__ = 'download_logs'

    id       = Column(String(36), primary_key=True)
    site     = Column(String(24))
    case     = Column(String(128))
    feed_id  = Column(String(256))
    createAt = Column(DateTime)

    def __init__(self, site, case, feed_id):
        self.id = str(uuid4())
        self.site = site
        self.case = case
        self.feed_id = feed_id
        self.createAt = datetime.now()
