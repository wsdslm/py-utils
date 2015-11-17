#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/5.
# python idm_dl <list_url>
import ConfigParser
import logging
import os
import sys
import time
from py_utils.libs.idm import Idm
from py_utils.pick.dmm import Dmm

list_url = sys.argv[1]

config = ConfigParser.RawConfigParser()
config.read(os.path.dirname(__file__) + '/pick.cfg')
save_path = config.get('dmm', 'save_path')
logging.basicConfig(level=logging.INFO)
covers = Dmm.get_list_covers(list_url)
for cover in covers:
    url = cover['link']
    ext = os.path.splitext(url)[1]
    filename = cover['title'] + ext
    Idm.add_file(url, filename, save_path)
    time.sleep(0.8)