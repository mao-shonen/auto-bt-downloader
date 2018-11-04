import os
import hashlib

users = os.environ.get('users', 'admin:admin') #user1:passwd1, user2:passwd2, ...

app_host = os.environ.get('app_host', '0.0.0.0')
app_port = int(os.environ.get('app_port', 5000))
app_secret_key = os.urandom(16)
app_debug = bool(os.environ.get('app_debug', False))

database_url = os.environ.get('database_url', 'sqlite:///case.db')
database_debug = bool(os.environ.get('database_debug', False))

qbittorrent_host = os.environ.get('qbittorrent_host', '127.0.0.1')
qbittorrent_port = os.environ.get('qbittorrent_port', '8080')
qbittorrent_user = os.environ.get('qbittorrent_user', 'admin')
qbittorrent_passwd = os.environ.get('qbittorrent_passwd', 'admin')

refresh = 300.0
request_intervals = 5.0
request_timeout = 30.0
request_retry = 3


#=============================================================
app_users = {}
for user in users.split(','):
    name, *passwd = user.strip().split(':')
    name = name.strip()
    passwd = ''.join(passwd).strip()

    sha256 = hashlib.sha256()
    sha256.update(passwd.encode())

    app_users[name] = sha256.hexdigest()
