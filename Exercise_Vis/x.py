import pandas as pd
import  matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np

dfAtlit = pd.read_csv('Atlit.csv')
dfCorr = dfAtlit.corr()
# dfCorr.dtypes
# dfCorr

# plt.figure(figsize=(35,10))
plt.imshow(dfCorr)
plt.colorbar()
col = list(map(lambda x: x, dfCorr.columns.tolist()))
plt.xticks(
    np.arange(len(dfCorr.index)),
    dfCorr.index.tolist(),
    rotation=45)
plt.yticks(
    np.arange(len(dfCorr.index)),
    dfCorr.index.tolist()
)

for x in range(len(col)):
    for y in range(len(col)):
        plt.text(y,x,round(dfCorr.iloc[x,y], 3),
                color='white',
                ha = 'center', va = 'center'
                )

plt.ylim(2.5,-0.5)   
plt.show()