from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from ._Base import Base


class DownloadLogs(Base):
    __tablename__ = 'download_logs'

    id       = Column(String(36), primary_key=True)
    site     = Column(String)
    case     = Column(String)
    feed_id  = Column(String)
    createAt = Column(DateTime)

    def __init__(self, site, case, feed_id):
        self.id = str(uuid4())
        self.site = site
        self.case = case
        self.feed_id = feed_id
        self.createAt = datetime.now()
