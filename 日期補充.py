# -*- coding:utf-8 -*-
import json,urllib
from urllib import urlencode
import pandas as pd
import datetime
import time
def cur(currency,time):
    url = 'http://api.k780.com'
    params = {
        'app': 'finance.rate_history',
        'curno': currency,
        'date': time,
        'appkey': '25894',
        'sign': 'c4e40e44956669ebf21f6c1ddf773350',
        'format': 'json',
    }
    params = urlencode(params)

    f = urllib.urlopen('%s?%s' % (url, params))
    nowapi_call = f.read()
    dat = json.loads(nowapi_call)
    return dat
#提取日期
def dayss(dataname):
    dat=dataname[u'result']
    dat = dat[0]
    tim = dat[u'days']
    t1 = str(tim)
    return t1
#提取汇率
def ratee(dataname):
    dat=dataname[u'result']
    dat = dat[0]
    rate = dat[u'rate']
    return rate

currency = "gbp"
d=20160324
file_nam=currency+".csv"
d1 = pd.read_csv(file_nam, header=None)
d2 = pd.read_csv(file_nam)
data=cur(currency,d)
day1=dayss(data)
rate1=ratee(data)
rate1=[rate1]
dat3 = pd.Series(rate1, name=day1)

d3 = pd.concat([d2, dat3], axis=1)
d3.to_csv(file_nam, index=False, encoding='utf-8')
