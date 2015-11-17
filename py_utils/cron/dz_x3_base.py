#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/12.
import requests
import time


class DzX3Base:
    base_url = 'http://bbs4.2djgame.net'
    apply_url = ''
    draw_url = ''

    def __init__(self,cookie,
                 agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'):
        session = requests.session()
        headers = {
            'User-Agent': agent,
            'Cookie': cookie
        }
        session.headers = headers
        self.session = session

    def task(self):
        self.session.get(self.apply_url)
        time.sleep(1)
        self.session.get(self.draw_url)
        print 'task complete'