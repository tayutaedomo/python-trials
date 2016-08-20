#! /usr/bin/env python
# -*- coding: utf-8 -*-

#
# Usage:
#   scripts/slack_send_request.py "<slack incoming webhook endpoint>"
#

import sys
import json
import urllib2

# Refer:
#   - http://stackoverflow.com/questions/7697963/how-to-debug-urllib2-request-that-uses-a-basic-authentication-handler
#   - http://stackoverflow.com/questions/1170744/how-do-i-get-urllib2-to-log-all-transferred-bytes
hh = urllib2.HTTPHandler()
hsh = urllib2.HTTPSHandler()
hh.set_http_debuglevel(1)
hsh.set_http_debuglevel(1)
opener = urllib2.build_opener(hh, hsh)
urllib2.install_opener(opener)


def send_request(url):
    try:
        headers = {
            'Content-type': 'application/json'
        }
        data = {
            'text': 'Send by Python',
            'username': 'Test Script',
            'icon_emoji': ':simple_smile:',
        }

        params = json.dumps(data)
        print 'params:', params

        req = urllib2.Request(url, params, headers)
        res = urllib2.urlopen(req)

        print res.read()
        print res.info().dict

    except urllib2.URLError, e:
        print e
        exit()


if __name__ == '__main__':
    url = sys.argv[1]
    print 'URL:', url

    send_request(url)

