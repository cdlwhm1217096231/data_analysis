#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-23 15:44:57
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$
import pandas as pd
import datetime
import pandas_datareader.data as web
import fix_yahoo_finance as fy
import numpy as np
import seaborn as sns
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


fy.pdr_override()
start = datetime.datetime(2014, 9, 19)
end = datetime.date.today()
alibaba = web.DataReader("BABA", "yahoo", start, end)
amazon = web.DataReader("AMZN", "yahoo", start, end)
# alibaba.to_csv('BABA1.csv')
# amazon.to_csv('AMZN1.csv')
print(alibaba.head())
alibaba['Adj Close'].plot(legend=True)
amazon['Adj Close'].plot(legend=True)
plt.show()
alibaba['Volume'].plot(legend=True)
plt.show()
alibaba['High-Low'] = alibaba['High'] - alibaba['Low']
print(alibaba.head())
alibaba['High-Low'].plot()
plt.show()
# 每天变化情况
alibaba['daily return'] = alibaba['Adj Close'].pct_change()
alibaba['daily return'].plot(figsize=(10, 4), linestyle='--', marker='o')
plt.show()

alibaba['daily return'].plot(kind='hist')
plt.show()

sns.distplot(alibaba['daily return'].dropna(), bins=100, color='purple')
plt.show()