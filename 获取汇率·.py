# -*- coding: utf-8 -*-
import json
import urllib
import pandas as pd
import datetime
import time


#返回货币代码
d1 = pd.read_csv("huiilv\huobidaima.csv",header=None)
le=len(d1)
for i in range(0,le):
    nam=d1[:i]