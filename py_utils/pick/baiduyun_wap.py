#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/10/25.
# 百度云批量转存，资源会转存到/我的资源/下
import json
import urlparse
import requests
import re


class BaiduyunWap:
    def __init__(self, bduss,
                 agent='Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'):
        session = requests.session()
        session.headers['User-Agent'] = agent
        session.cookies['BDUSS'] = bduss
        self._bduss = bduss
        self._session = session

    def save(self, url, code=None):
        if self._check_init(url):
            self._access_code(url, code)
        content = self._session.get(url).content
        dbstoken = self._get_bdstoken(content)
        shareid = self._get_shareid(content)
        uk = self._get_uk(content)
        filelist = self._get_filelist(content)
        params = {
            'shareid': shareid,
            'from': uk,
            'bdstoken': dbstoken,
            'channel': 'chunlei',
            'clienttype': 5,
            'web': 1
        }
        data = {
            'filelist': filelist,
            'path': '/我的资源/',
            'type': 1,
            'async': 1
        }
        r = self._session.post('http://pan.baidu.com/share/transfer', params=params, data=data)
        print r.content

    def _check_init(self, url):
        r = self._session.get(url)
        return urlparse.urlparse(r.url).path == '/wap/init'

    def _access_code(self, url, code):
        r = self._session.get(url)
        init_url = r.url
        querys = urlparse.parse_qs(urlparse.urlparse(init_url).query)
        shareid = querys['shareid']
        uk = querys['uk']
        params = {
            'shareid': shareid,
            'uk': uk,
            'channel': 'chunlei',
            'clienttype': 5,
            'web': 1
        }
        data = {
            'pwd': code,
            'vcode': ''
        }
        self._session.post('http://pan.baidu.com/wap/verify', params=params, data=data)

    def _get_bdstoken(self, content):
        pattern = r'bdstoken="(.*?)"'
        matches = re.search(pattern, content)
        return matches.group(1)

    def _get_shareid(self, content):
        pattern = r'FileUtils\.shareid="(\d*)"'
        matches = re.search(pattern, content)
        return matches.group(1)

    def _get_app_id(self, content):
        pattern = r'\\"app_id\\":\\"(\d*)\\"'
        matches = re.search(pattern, content)
        return matches.group(1)

    def _get_uk(self, content):
        pattern = r'FileUtils\.uk="(.*?)"'
        matches = re.search(pattern, content)
        return matches.group(1)

    def _get_filelist(self, content):
        pattern = r'\\"path\\":\\"(.*?)\\"'
        matches = re.search(pattern, content)
        str = matches.group(1).decode('string_escape')
        return '["' + json.loads('"' + str + '"') + '"]'