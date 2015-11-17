#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/5.
# https://www.internetdownloadmanager.com/
import locale
import logging
import subprocess


class Idm:
    bin_path = 'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'

    @classmethod
    def add_file(cls, url, filename='', save_path=''):
        encoding = locale.getdefaultlocale()[1]
        cmd = u'"%s" /a /d %s' % (cls.bin_path, url)
        if '' != filename:
            if '' != save_path:
                cmd = u'"%s" /a /p "%s" /f "%s" /d %s' % (cls.bin_path, save_path, filename, url)
            else:
                cmd = u'"%s" /a /f "%s" /d %s' % (cls.bin_path, filename, url)
        subprocess.call(cmd.encode(encoding))
        logging.info('add to idm:' + url)