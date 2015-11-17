#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/11/12.
from py_utils.cron.dz_x3_base import DzX3Base


class LightNovel(DzX3Base):
    base_url = 'http://www.lightnovel.cn'
    apply_url = base_url + '/home.php?mod=task&do=apply&id=98'
    draw_url = base_url + '/home.php?mod=task&do=draw&id=98'