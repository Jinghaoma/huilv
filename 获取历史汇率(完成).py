# -*- coding:utf-8 -*-
import json,urllib
from urllib import urlencode
import pandas as pd
import datetime
import time

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
#给定日期返回下1天
def tim(time):
    t1 = time
    year = int(t1[0:4])
    month = int(t1[4:6])
    day = int(t1[6:8])
    d1 = datetime.date(year, month, day)
    delta = datetime.timedelta(days=1)
    s2=d1+delta
    st = s2.strftime("%Y%m%d")
    return st
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
#读取到了哪一天
def da(file_name):
    d1 = pd.read_csv(file_name, header=None)
    d2 = d1.iat[0, -1]
    d2 = d2[0:4] + d2[5:7] + d2[8:10]
    return d2
#倒计时 每100秒提示
def dow(tim):
    for i in range(tim):
        x1 = tim - i
        time.sleep(1)
        if x1 % 100 == 0:
            print x1
#获取货币名称
def name1(file_name):
    d1 = pd.read_csv(file_name, header=None)
    d2 = d1.iat[1,0]
    d2=d2.lower()
    return d2
#判断日期是否等于昨天的日期 等于true
def now_day(time):
    t1 = time
    year = int(t1[0:4])
    month = int(t1[4:6])
    day = int(t1[6:8])
    d1 = datetime.date(year, month, day)
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d')
    now = datetime.date(int(now[0:4]), int(now[5:7]), int(now[8:10]))
    dif = now - d1
    dif = dif.days
    if dif <= 1:
        return False
    else:
        return True

currency = "rub"
file_nam=currency+".csv"
nam=name1(file_nam)
dat_all = pd.read_csv(file_nam)
day = da(file_nam)

n=True
while n:
    day1=day
    day = tim(day)
    n = now_day(day)
    data1 = cur(currency, day)
    day_out = day[0:4] + "-" + day[4:6] + "-" + day[6:8]
    if data1:
        if data1['success'] != '0':
            print "正在获取%s的数据" % day_out
            da1 = dayss(data1)
            ra1 = ratee(data1)
            ra1 = [ra1]
            dat3 = pd.Series(ra1, name=da1)
            dat_all = addd(dat_all, dat3)
            time.sleep(3)
            dat_all.to_csv(file_nam, index=False, encoding='utf-8')
        else:
            if data1[u'msgid'] == u'1000060':
                print data1['msgid'] + ' ' + data1['msg']
                dat3 = pd.Series(["NA"], name=day_out)
                dat_all = addd(dat_all, dat3)
                dat_all.to_csv(file_nam, index=False, encoding='utf-8')
            if data1[u'msgid'] == u'1000701':
                print data1['msgid'] + ' ' + data1['msg']
                day = day1
                print "等待"
                dow(3700)
    else:
        print 'Request nowapi fail.';
        break

