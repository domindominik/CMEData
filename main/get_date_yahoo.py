import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2014, 1, 1)
stop = dt.datetime(2020, 3, 18)

df = web.DataReader('TSLA', 'yahoo', start, stop)

df.to_csv('tsla.csv')
print(df)