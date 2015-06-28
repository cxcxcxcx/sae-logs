#!/usr/bin/env python
import argparse
import cStringIO
import hashlib
import json
import os
import re
import tarfile
import urllib2


parser = argparse.ArgumentParser(description='Download sae logs.')
parser.add_argument('--appname', help='SAE app name')
parser.add_argument('--from_date', help='from date')
parser.add_argument('--to_date', help='to date')
parser.add_argument('--secret_key', help='secret key')
parser.add_argument('--output_path', help='output path')
args = parser.parse_args()


def get_signature(request, secret_key):
    sign = request.replace('&','')
    sign += secret_key

    md5 = hashlib.md5()
    md5.update(sign)
    return md5.hexdigest()

api_url = 'http://dloadcenter.sae.sina.com.cn/interapi.php?'
params = {
    'act': 'log',
    'appname': args.appname,
    'from': args.from_date,
    'to': args.to_date,
    'type': 'http',
    'type2': 'access',
}

request = '&'.join([k + '=' + v for k, v in sorted(params.items())])
request_url = api_url + request + '&sign=' + get_signature(request, args.secret_key)

# request api
response = json.load(urllib2.urlopen(request_url))
if response['errno'] != 0:
    print response
    os.exit()
print '[#] request success'

for down_url in response['data']:
    file_date = re.compile(r'\d{4}-\d{2}-\d{2}').findall(down_url)[0]
    print('Processing %s' % down_url)
    tar = tarfile.open(
            fileobj=cStringIO.StringIO(
                urllib2.urlopen(down_url).read()))
    tar.extract(tar.getnames()[0], args.output_path + '/access_log_' + file_date)
