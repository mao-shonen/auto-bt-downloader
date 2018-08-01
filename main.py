import yaml
from time import sleep
from utils import logger
import config

import threading
import requests
import feedparser
from database import db_connect, DownloadLogs
from models import Qbittorrent

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.cases = config.case_loader()

    def run(self):
        self.dmhy()

    def dmhy(self):
        site = '動漫花園'

        for case, keys in self.cases[site].items():
            logger.info('搜尋 %s', case)

            for _ in range(config.request_retry):
                try:
                    html = requests.get('https://share.dmhy.org/topics/rss/rss.xml', params={'keyword':keys}, timeout=config.request_timeout)
                    break
                except Exception as e:
                    logger.warn('request %s fail: %s' % (site, e))
            else:
                return False
            rss_feed = feedparser.parse(html.text)

            for i in rss_feed['entries']:
                feed_id = i['id']
                title = i['title']
                magnet_link = i['links'][1]['href']

                self.download(site, case, feed_id, title, magnet_link)

            sleep(config.request_intervals)
                
                
    def download(self, site, case, feed_id, title, magnet_link):
        db = db_connect()
        dl = db.query(DownloadLogs).filter_by(site=site, case=case, feed_id=feed_id).first()
        if dl:
            db.close()
            return False

        logger.info('downloading %s' % (title))

        try:
            bt = Qbittorrent(
                host     = config.qbittorrent_host,
                port     = config.qbittorrent_port,
                username = config.qbittorrent_user,
                password = config.qbittorrent_passwd,
            ) 
        except Exception as e:
            logger.warn('qbittorrent login fail: %s' % e)
            return False

        bt.download_from_url(magnet_link, category=case)

        try:
            row = DownloadLogs(site, case, feed_id)
            db.add(row)
            db.commit()
        except Exception as e:
            db.rollback()

        db.close()
        return True


while True:
    task = Worker()
    task.start()
    task.join()
    logger.info('next task on %ss after' % config.refresh)
    sleep(config.refresh)
