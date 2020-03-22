import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import style

style.use('ggplot')

def visualize_data():
    df = pd.read_csv('stock_dfs/sp500_joined_closes.csv')
    df_corr = df.corr()
    print(df_corr)
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1,)
    heat_map = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heat_map)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    column_labels = df_corr.columns
    row_labels = df_corr.index
    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heat_map.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()

visualize_data()