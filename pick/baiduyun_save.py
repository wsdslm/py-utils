#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/6.
import ConfigParser
import os
from py_utils.pick.baiduyun_wap import BaiduyunWap

config = ConfigParser.RawConfigParser()
config.read(os.path.dirname(__file__) + '/pick.cfg')
bduss = config.get('baiduyun_wap', 'bduss')
yun = BaiduyunWap(bduss)
url = 'http://pan.baidu.com/s/1o6IJcNo'
code = 't47o'
try:
    yun.save(url, code)
    print url, 'save success'
except:
    print url, 'save fail'