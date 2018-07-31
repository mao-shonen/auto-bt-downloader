from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ._Base import Base
from .DownloadLogs import DownloadLogs


engine = create_engine('sqlite:///case.db', echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def db_connect():
    return Session()