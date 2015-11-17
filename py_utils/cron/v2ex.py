#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/10/25.
import requests
import re


class V2ex:
    base_url = 'http://www.v2ex.com'

    def __init__(self, cookie,
                 agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0'):
        session = requests.session()
        headers = {
            'User-Agent': agent,
            'Cookie': cookie
        }
        session.headers = headers
        self.session = session

    def task(self):
        mission_url = self._get_mission_url()
        print mission_url
        # self._start_mission(mission_url)
        print 'task complete'

    def _start_mission(self, mission_url):
        self.session.headers['referer'] = self.base_url + '/mission/daily'
        r = self.session.get(mission_url)
        print r.text

    def _get_mission_url(self):
        r = self.session.get(self.base_url + '/mission/daily')
        box_pattern = r'/mission/daily/redeem\?once=\d+'
        matches = re.search(box_pattern, r.text)
        return self.base_url + matches.group(0) if None != matches else ''