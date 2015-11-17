#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/10/25.
import requests
import re


class Feiyue:
    base_url = 'http://2dgal.com'

    def __init__(self, username, password,
                 agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0'):
        self.username = username
        self.password = password
        session = requests.session()
        headers = {
            'User-Agent': agent,
        }
        session.headers = headers
        self.session = session

    def task(self):
        self._login()
        self._click_smbox()
        self._groupup()
        print 'task complete'

    def _click_smbox(self):
        box_url = self._get_box_url()
        self.session.get(box_url)

    def _groupup(self):
        data = {
            'submit': '确定捐款',
            'kfb': 5
        }
        self.session.post(self.base_url + '/kf_growup.php?ok=1', data)

    def _login(self):
        data = {
            'step': 2,
            'lgt': 1,
            'pwuser': self.username,
            'pwpwd': self.password,
            'hideid': 0,
            'cktime': 0,
            'submit': '登 录'
        }
        self.session.post(self.base_url + '/login.php?', data)


    def _get_box_url(self):
        r = self.session.get(self.base_url + '/kf_smbox.php')
        r.encoding = 'gbk'
        box_pattern = '\"(kf_smbox\.php\?box=.*?)\"'
        matches = re.search(box_pattern, r.text)
        return self.base_url + '/' + matches.group(1)