#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/6.
import ConfigParser
import logging
import os
import sys
import time
from py_utils.libs.idm import Idm
from py_utils.pick.pixiv import Pixiv

search_url = sys.argv[1]

logging.basicConfig(level=logging.DEBUG)
config = ConfigParser.RawConfigParser()
config.read(os.path.dirname(__file__) + '/pick.cfg')
agent = config.get('pixiv', 'agent')
cookie = config.get('pixiv', 'cookie')
save_path = config.get('pixiv', 'save_path')
p = Pixiv(cookie, agent)
images = p.get_search_images(search_url)
for image in images:
    Idm.add_file(image, os.path.basename(image), save_path)
    time.sleep(0.8)