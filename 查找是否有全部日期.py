# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:04:12 2017

@author: OWNER
"""

import json,urllib
from urllib import urlencode
import pandas as pd
import datetime
import time
currency = "123"
file_nam=currency+".csv"
d1 = pd.read_csv(file_nam, header=None)
dd2=datetime.date(2015,12,12)
delta = datetime.timedelta(days=1)
dd2 = datetime.date(2015, 12, 12)
i=True
j=1

while i is True:
    d2=d1.iat[0,j]
    year = int(d2[0:4])
    month = int(d2[5:7])
    day = int(d2[8:10])
    dd1 = datetime.date(year, month, day)
    if dd1==dd2:
        i=True
        j+=1
        print dd2,"same"
        dd2 = dd2 + delta
    else:
        i=False
        print dd2,j
