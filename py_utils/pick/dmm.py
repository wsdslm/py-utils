#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/5.
# http://www.dmm.co.jp/
import re
import requests
import bs4


class Dmm:
    def __init__(self):
        pass

    @classmethod
    def get_list_covers(list_url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
        }
        r = requests.get(list_url, headers=headers)
        content = r.content.decode('euc-jp')
        soup = bs4.BeautifulSoup(content, 'html.parser')
        for img in soup.select('#list img'):
            yield {
                'title': img['alt'],
                'link': re.sub(r'pt\.jpg$', 'pl.jpg', img['src'])
            }