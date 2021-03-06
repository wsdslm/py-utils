#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/12.
import ConfigParser
from os import path
from py_utils.cron.v2ex import V2ex


if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read(path.dirname(__file__) + '/cron.cfg')
    cookie = config.get('v2ex', 'cookie')
    v = V2ex(cookie)
    v.task()