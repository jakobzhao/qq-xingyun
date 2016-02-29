# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Oct 16, 2015
# @author:       Bo Zhao
# @email:        bo_zhao@hks.harvard.edu
# @website:      http://yenching.org
# @organization: Harvard Kennedy School

from pytz import timezone
TZCHINA = timezone('Asia/Chongqing')
UTC = timezone('UTC')
TIMEOUT = 5

BAIDU_AK = 'Y4wB8DznamkwhY8RxDiYNSHS'
# BAIDU_AK = 'fGnFQVLoY6AgmPM1spgYvsD9'
PB_KEY = 'bYJFjyvIYWbn5vg2eNiFmcapjLu1PUTL'
EMAIL_PASSWORD = 'nanjing1212'
STOP_WORDS = list(u' ：@:～~：:。·-—，,？?！!&*#[]；;：:、“”【】[]《》<>|()（）⊙▽…/↓→=_的了吗咯哦呗')
STOP_WORDS.extend([u'http', u'...'])