import requests


class Qbittorrent:
    def __init__(self, host='127.0.0.1', port=8080, username=None, password=None, timeout=5.0):
        self.host = '%s:%s' % (host, port) if ':' not in host else host
        if host[:4] != 'http':
            self.host = 'http://' + self.host
        self.timeout = timeout

        if username and password:
            self.login(username, password)

    def _get(self, endpoint, **kwargs):
        return self.session.get(self.host + endpoint, params=kwargs, timeout=self.timeout)

    def _post(self, endpoint, data=None, **kwargs):
        return self.session.post(self.host + endpoint, data=data, **kwargs, timeout=self.timeout)

    def login(self, username=None, password=None):
        self.session = requests.Session()
        r = self._post('/login', data={'username':username, 'password':password})
        if r.ok and r.text == 'Ok.':
            return True
        raise Exception(r.text)

    def torrnets(self, **kwargs):
        r = self._get('/query/torrents', **kwargs)
        if r.ok:
            return r.text
        raise Exception('ERROR qbittorrent torrents')

    def download_from_url(self, urls, **kwargs):
        kwargs['urls'] = urls
        r = self._post('/command/download', data=kwargs)
        if r.ok:
            return True
        raise Exception('ERROR qbittorrent download on %s' % (urls))
    