#!/usr/bin/env python
# coding=utf-8
# Created by wsdslm <wsdslm@gmail.com> on 2015/10/25.
from py_utils.cron.dz_x3_base import DzX3Base


class Djgame(DzX3Base):
    base_url = 'http://bbs4.2djgame.net'
    apply_url = base_url + '/home/home.php?mod=task&do=apply&id=1'
    draw_url = base_url + '/home/home.php?mod=task&do=draw&id=1'