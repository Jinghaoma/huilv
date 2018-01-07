# -*- coding:utf-8 -*-
import json,urllib
from urllib import urlencode
import pandas as pd

#给定货币代码和日期返回当当天货币
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
#提取货币名称
def curnoo(dataname):
    dat=dataname[u'result']
    dat = dat[0]
    name = dat[u'curno']
    return name
#合并数据
def addd(dataname1,dataname2):
    data = pd.concat([dataname1, dataname2], axis=1)
    return data

currency="rub"
day="20151212"
file_name=currency+".csv"

data=cur(currency,day)

day1=dayss(data)
rate1=ratee(data)
cur=curnoo(data)

rate1 = [rate1]
cur=[cur]
dat2 = pd.Series(rate1, name=day1)
dat3 = pd.Series(cur, name="curno")
dat_all = addd(dat3, dat2)
dat_all.to_csv(file_name, index=False, encoding='utf-8',mode='w')
