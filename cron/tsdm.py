#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2016/7/11.
import ConfigParser

from os import path

from py_utils.cron.tsdm import Tsdm

if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read(path.dirname(__file__) + '/cron.cfg')
    cookie = config.get('tsdm', 'cookie')
    lk = Tsdm(cookie)
    lk.sign()
