# -*- coding:utf-8 -*-
import json
import urllib
from urllib import urlencode
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://api.k780.com'
params = {
  'app' : 'finance.rate_curlist',
  'appkey' : '25894',
  'sign' : 'c4e40e44956669ebf21f6c1ddf773350',
  'format' : 'json',
}
params = urlencode(params)

f = urllib.urlopen('%s?%s' % (url, params))
nowapi_call = f.read()
#print content
dat = json.loads(nowapi_call)

json_string=json.dumps(dat)
data=json.loads(json_string)
data123=data[u'result']
data456=json.dumps(data123,ensure_ascii=False)

f = file("汇率.csv","w")
for i in range(0,160):
    d1=data123[i]
    d1curnm=d1[u'curnm']
    d1curno=d1[u'curno']
    f.write(d1curnm)
    f.write(",")
    f.write(d1curno)
    f.write("\n")
f.close()