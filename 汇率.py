import json,urllib
from urllib import urlencode

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

a_result = json.loads(nowapi_call)