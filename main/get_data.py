from simplefix import *
import pandas_datareader as pdr
import pandas as pd
import datetime as dt

start = dt.datetime(2010, 1, 1)
end = dt.datetime(2020, 3, 17)

df = pdr.DataReader("TSLA", 'yahoo', start, end)
print(df.tail(6))

