import pandas as pd
import matplotlib.pyplot as plt
import simplefix as sf
from simplefix import *

#data_feed = pd.read_csv('/home/dominik/PycharmProjects/CMEData/6E_20060207.TXT', delimiter="\t")
data_feed = pd.open('/home/dominik/PycharmProjects/CMEData/6E_20060207.TXT', 'r')
data_feed = data_feed.decode('utf-8')
print(data_feed)

#cme_data = sf.FixParser.add_raw('6E_20060207.TXT')

#data_feed.plot()
#plt.show()

