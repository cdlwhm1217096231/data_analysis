#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-23 01:56:38
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$
import pandas as pd
import datetime
import pandas_datareader.data as web
import fix_yahoo_finance as fy

fy.pdr_override()
start = datetime.datetime(2014, 9, 19)
end = datetime.date.today()
alibaba = web.DataReader("BABA", "yahoo", start, end)
print(alibaba.head())
print(alibaba.shape)
print(alibaba.tail())
print(alibaba.describe())
print(alibaba.info())

