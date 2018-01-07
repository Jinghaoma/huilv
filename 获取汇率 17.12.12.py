#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib
import pandas as pd
import datetime
import time


def mget_exchange_rate():
    # 获得汇率
    api_key = "NS8pcpi31jc9qYA7oy3Jh8p4YEdCYeUS"
    typ = "USDJPY,EURJPY,GBPJPY,AUDJPY,NZDJPY,CHFJPY,CADJPY,ZARJPY,TRYJPY," \
          "USDCHF,USDCAD,EURGBP,EURAUD,EURNZD,EURCHF,GBPAUD,GBPCHF,EURUSD,GBPUSD,AUDUSD,NZDUSD," \
          "CNHUSD,CNHEUR,CNHJPY,CNHGBP,CNHCHF,CNHAUD,CNHCAD,CNHNZD,CNHSEK,CNHNOK,CNHMXN,CNHZAR,CNHTRY,CNHXAU,CNHXAG"
    f = urllib.request.urlopen("https://forex.1forge.com/1.0.2/quotes?pairs=%s&api_key=%s" % (typ, api_key))
    nowapi_call = f.read()
    dat = json.loads(nowapi_call)
    return dat


def get_time_jp(name):
    # 获得日本时间，时间戳转换
    f1 = name[1]
    timeStamp = f1["timestamp"]
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


def get_rank(name, abp="ask"):
    # 获得ask价格的字典
    symbol = []
    ass = []
    for i in name:
        symbol.append(i["symbol"])
        ass.append(i[abp])
    ask = {}
    for t in range(len(symbol)):
        ask[symbol[t]] = ass[t]
    return ask


def first_run_pro(go_time='2017-12-20 19:53'):
    # 执行程序
    while True:
        now_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
        if go_time == now_time:
            er = mget_exchange_rate()
            tim = get_time_jp(er)
            ask = get_rank(er, abp="ask")
            bid = get_rank(er, abp="bid")
            price = get_rank(er, abp="price")
            ask = pd.Series(ask)
            bid = pd.Series(bid)
            price = pd.Series(price)
            ask = pd.DataFrame(ask, columns=[pd.to_datetime(tim)]).T
            bid = pd.DataFrame(bid, columns=[pd.to_datetime(tim)]).T
            price = pd.DataFrame(price, columns=[pd.to_datetime(tim)]).T
            ask.to_csv("ask.csv", encoding='utf-8')
            bid.to_csv("bid.csv", encoding='utf-8')
            price.to_csv("price.csv", encoding='utf-8')
            break
        else:
            print("no")
            time.sleep(1)
    # 获取现在时间，在整点时开始执行程序


def no_first_run_pro(sleeptime=180):
    time.sleep(sleeptime)
    while True:
        er = mget_exchange_rate()
        tim = get_time_jp(er)
        ask = get_rank(er, abp="ask")
        bid = get_rank(er, abp="bid")
        price = get_rank(er, abp="price")
        ask = pd.Series(ask)
        bid = pd.Series(bid)
        price = pd.Series(price)
        ask = pd.DataFrame(ask, columns=[pd.to_datetime(tim)]).T
        bid = pd.DataFrame(bid, columns=[pd.to_datetime(tim)]).T
        price = pd.DataFrame(price, columns=[pd.to_datetime(tim)]).T
        ask.to_csv("ask.csv", encoding='utf-8', mode="a", header=False)
        bid.to_csv("bid.csv", encoding='utf-8', mode="a", header=False)
        price.to_csv("price.csv", encoding='utf-8', mode="a", header=False)
        print(tim)
        time.sleep(sleeptime)

    # 获取现在时间，在整点时开始执行程序


first_run_pro("2017-12-20 20:05")
no_first_run_pro()
