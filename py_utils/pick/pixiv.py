#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/6.
# http://www.pixiv.net/
import requests
import bs4


class Pixiv:
    base_url = 'http://www.pixiv.net'

    def __init__(self, cookie, agent):
        headers = {
            'User-Agent': agent,
            'Cookie': cookie
        }
        self.session = requests.session()
        self.session.headers = headers

    def get_search_images(self, search_url):
        content = self.session.get(search_url).text
        soup = bs4.BeautifulSoup(content, 'html.parser')
        links = soup.select('.image-item a')
        for link in links:
            if link.find('img'):
                img = self._get_medium_image(self.base_url + link['href'])
                if img:
                    yield img
                else:
                    manga_link = link['href'].replace('mode=medium', 'mode=manga')
                    imgs = self._get_manga_images(self.base_url + manga_link)
                    for img in imgs:
                        yield img

    def _get_medium_image(self, url):
        content = self.session.get(url).text
        soup = bs4.BeautifulSoup(content, 'html.parser')
        img = soup.select_one('._illust_modal.ui-modal-close-box img')
        return img['data-src'] if img else None

    def _get_manga_images(self, url):
        content = self.session.get(url).text
        soup = bs4.BeautifulSoup(content, 'html.parser')
        imgs = soup.select('.image')
        for img in imgs:
            yield img['data-src']