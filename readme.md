# readme #
日常任务和采集工具

- [绯月Galgame](http://2dkf.com/)
- [轻之国度](http://www.lightnovel.cn/forum.php)
- [2DJGAME!](http://bbs4.2djgame.net/home/forum.php)
- [V2EX](https://www.v2ex.com/)
- [天使动漫论坛](http://www.tsdm.net/forum.php)

## 使用 ##
获取代码

    cd ~
    git clone https://github.com/wsdslm/py-utils.git
    cd py-utils
    pip install .
    # 卸载
    #pip uninstall py-utils

## 日常任务 ##

	vi cron/cron.cfg
	crontab -e
	5 */5 * * * python ~/py-utils/cron/feiyue.py
	5 0 * * * python ~/py-utils/cron/lk.py
	5 0 * * * python ~/py-utils/cron/djgame.py
	5 0 * * * python ~/py-utils/cron/v2ex.py
	5 0 * * * python ~/py-utils/cron/tsdm.py

## 采集 ##
Windows下配合IDM使用

    vi pick/pick.cfg
	python pick/pixiv_dl.py <search_url>
	python pick/dmm.py <list_url>
