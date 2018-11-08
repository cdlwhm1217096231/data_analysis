#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import pandas as pd
import datetime
import pandas_datareader.data as web
import fix_yahoo_finance as fy
import numpy as np
import seaborn as sns
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

fy.pdr_override()
start = datetime.datetime(2015, 1, 1)
end = datetime.date.today()
company = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'FB']
top_teach_df = web.DataReader(company, "yahoo", start, end)['Adj Close']
# top_teach_df.to_csv('top5_1.csv')
print(top_teach_df.tail())
# 每天变化
top_teach_dr = top_teach_df.pct_change()
print(top_teach_dr.head())
top_teach_df.plot()
plt.show()

top_teach_df[['AAPL', 'FB', 'MSFT']].plot()
plt.show()

# 散点图分析是否具有相关性
sns.jointplot('MSFT', 'FB', top_teach_dr, kind='scatter')
plt.show()

# 散点图分析是否具有相关性
sns.pairplot(top_teach_dr.dropna())
plt.show()

# 风险评估
print(top_teach_dr['AAPL'].quantile(0.52))

print(top_teach_dr['MSFT'].quantile(0.05))  # 有95%的信心，让最大亏损是MSFT

vips = web.DataReader("VIPS", "yahoo", start, end)['Adj Close']
vips.plot()
plt.show()
print(vips.pct_change().quantile(0.2))