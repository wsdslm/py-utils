#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/12.
import ConfigParser
from os import path
from py_utils.cron.feiyue import Feiyue

if __name__ == '__main__':
    config = ConfigParser.ConfigParser()
    config.read(path.dirname(__file__) + '/cron.cfg')
    username = config.get('feiyue', 'username')
    password = config.get('feiyue', 'password')

    f = Feiyue(username, password)
    f.task()