# !/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created on Feb 29, 2016
# @author:       Bo Zhao
# @email:        bo_zhao@hks.harvard.edu
# @website:      http://yenching.org
# @organization: Harvard Kennedy School

import urllib

from pymongo import MongoClient, errors
from log import *
from settings import TZCHINA
import datetime
import random
import urllib2
import json


# Crawling pages from http://xingyun.map.qq.com/
def qqcrawler(project, address, port):
    start = datetime.datetime.now()
    log(NOTICE, u'Crawling 腾讯地图开放平台 当日定位次数http://xingyun.map.qq.com/....')

    client = MongoClient(address, port)
    db = client[project]

    headers = [
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; InfoPath.1',
        'Mozilla/4.0 (compatible; GoogleToolbar 5.0.2124.2070; Windows 6.0; MSIE 8.0.6001.18241)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; Sleipnir/2.9.8)'
    ]
    random_header = random.choice(headers)

    base_url = "http://xingyun.map.qq.com/api/getPointsByTime_all_new.php?count=4&rank=0&time="
    now = datetime.datetime.now(TZCHINA) - datetime.timedelta(minutes=10)
    timestring = now.strftime('%Y-%m-%d %H:%M:00')
    url = base_url + urllib.quote(timestring)

    req = urllib2.Request(url)
    req.add_header("User-Agent", random_header)
    content = urllib2.urlopen(req, timeout=60).read()
    qq_json = json.loads(content)

    # arr = qq_json['locs'].split(",")
    # num = len(arr) / 3
    # i = 0
    # timestamp = qq_json['time']
    # while i < num:
    #     lat = float(int(arr[i * 3])/100.0)
    #     lng = float(int(arr[i * 3 + 1])/100.0)
    #     cnt = int(arr[i * 3 + 1])
    #     i += 1
    #     insert_json = {
    #         'timestamp': timestamp,
    #         'lat': lat,
    #         'lng': lng,
    #         'cnt': cnt
    #     }
    #     try:
    #         db.pages.insert_one(insert_json)
    #         log(NOTICE, '(%f, %f), count= %d' % (lat, lng, cnt))
    #     except errors.DuplicateKeyError:
    #         log(NOTICE, 'This post has already been inserted.')

    try:
        db.pages.insert_one(qq_json)
        log(NOTICE, qq_json['time'])
    except errors.DuplicateKeyError:
        log(NOTICE, 'This post has already been inserted.')

    log(NOTICE, 'Mission completion. Time: %d sec(s)' % int((datetime.datetime.now() - start).seconds))