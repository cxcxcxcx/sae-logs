#!/usr/bin/env python2
import argparse
import hashlib
import cStringIO
# import io
import json
import sys
import re
import tarfile
from apibus_handler import SaeApibusAuthHandler
import urllib2


parser = argparse.ArgumentParser(description='Download sae logs.')
parser.add_argument('--logs_type', help='storage,http,etc')
parser.add_argument('--from_date', help='from date')
parser.add_argument('--to_date', help='to date')
parser.add_argument('--access_key', help='access key')
parser.add_argument('--secret_key', help='secret key')
parser.add_argument('--output_path', help='output path')
args = parser.parse_args()


apibus_handler = SaeApibusAuthHandler(args.access_key, args.secret_key)
opener = urllib2.build_opener(apibus_handler)
response = json.load(opener.open('http://g.sae.sina.com.cn/log/%s/%s:%s/1-access' % (args.logs_type, args.from_date, args.to_date)))


for down_url in response['Content']:
    # file_date = re.compile(r'\d{4}-\d{2}-\d{2}').findall(down_url)[0]
    file_date = down_url['date']
    print('Processing %s' % down_url)
    tar = tarfile.open(
            fileobj=cStringIO.StringIO(
                urllib2.urlopen('http://g.sae.sina.com.cn' + down_url['uri']).read()))
    tar.extract(tar.getnames()[0], args.output_path + '/access_log_' + file_date)
