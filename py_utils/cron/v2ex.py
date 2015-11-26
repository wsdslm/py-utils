#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/10/25.
import requests
import re


class V2ex:
    base_url = 'http://www.v2ex.com'

    def __init__(self, cookie,
                 agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'):
        session = requests.session()
        session.headers['user-agent'] = agent
        session.headers['cookie'] = cookie
        self._session = session

    def task(self):
        mission_url = self._get_mission_url()
        self._start_mission(mission_url)
        print 'task complete'

    def _start_mission(self, mission_url):
        self._session.headers['referer'] = self.base_url + '/mission/daily'
        self._session.get(mission_url)

    def _get_mission_url(self):
        r = self._session.get(self.base_url + '/mission/daily')
        box_pattern = r'/mission/daily/redeem\?once=\d+'
        matches = re.search(box_pattern, r.text)
        return self.base_url + matches.group(0) if None != matches else ''