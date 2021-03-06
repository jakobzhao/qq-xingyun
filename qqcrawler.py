# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Feb 25, 2016
# @author:       Bo Zhao
# @email:        bo_zhao@hks.harvard.edu
# @website:      http://yenching.org
# @organization: Harvard Kennedy School

from qqcrawler.qq import qqcrawler
from qqcrawler.log import *
import datetime
import sys
import time
sys.path.append("/usr/local/lib/python2.7/site-packages")
sys.path.append("/home/Workspace/qqcrawler")

port = 27017
address = 'localhost'
project = 'qq'


start = datetime.datetime.now()
log(NOTICE, 'QQ Xingyun Crawler Initializing...')

while True:
    qqcrawler(project, address, port)
    time.sleep(300)

log(NOTICE, 'Mission completes. Time: %d sec(s)' % (int((datetime.datetime.now() - start).seconds)))

if __name__ == '__main__':
    pass
