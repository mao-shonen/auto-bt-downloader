import os
import yaml


database_url = os.environ.get('database_url', 'sqlite:///case.db')

qbittorrent_host = os.environ.get('qbittorrent_host', '127.0.0.1')
qbittorrent_port = os.environ.get('qbittorrent_port', '8080')
qbittorrent_user = os.environ.get('qbittorrent_user', 'admin')
qbittorrent_passwd = os.environ.get('qbittorrent_passwd', 'admin')

refresh = 300.0
request_intervals = 5.0
request_timeout = 30.0
request_retry = 3

def case_loader():
    return yaml.load(open('config.yml', 'r', encoding='utf-8-sig'))
