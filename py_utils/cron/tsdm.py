#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2016/7/3.
import urllib
import requests
import bs4


class Tsdm:
    base_url = 'http://www.tsdm.net'
    sign_url = base_url + '/plugin.php?id=dsu_paulsign:sign'

    def __init__(self, cookie,
                 agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'):
        session = requests.session()
        session.headers['user-agent'] = agent
        session.headers['cookie'] = cookie
        self._session = session

    def sign(self):
        url = self.base_url + '/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1'
        data = {
            'formhash': self._get_formhash(),
            'qdxq': 'yl',
            'qdmode': 1,
            'todaysay': 'qiandao',
            'fastreply': '1'
        }
        self._session.headers['referer'] = self.sign_url
        self._session.post(url, data)
        print 'task complete'

    def _get_formhash(self):
        r = self._session.get(self.sign_url)
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        el = soup.select('input[name=formhash]')
        return el[0]['value']


if __name__ == '__main__':
    cookie = ''
    t = Tsdm(cookie)
    t.sign()
