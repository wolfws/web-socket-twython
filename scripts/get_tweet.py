#!/usr/bin/python3
#-*- coding: utf-8 -*-

from twython import Twython
import json
import config as c


twitter = Twython(c.CONSUMER_KEY, c.CONSUMER_SECRET, c.ACCESS_TOKEN,
        c.ACCESS_SECRET )

result = twitter.search(q='http://www.mynet.com/my/alihalitdiker/hangi-iett-hattisin-1037329')
for status in result["statuses"]:
    print("%d %s" % (status["id"],status["text"]))
