#Stock Prices
import datetime as dt
from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')
start=dt.datetime(2018,1,1)
end=dt.datetime(2019,1,1)
#df=web.DataReader('GOOGL','yahoo',start,end)
#df.to_csv('GOOGL.csv')
df=pd.read_csv('AMZN.csv',parse_dates=True,index_col=0)
df[['Open','Close']].plot()
plt.show()
df['100ma']=df['Adj Close'].rolling(window=100).mean()
ax1=plt.subplot2grid((20,1),(0,0),rowspan=5,colspan=1)
ax2=plt.subplot2grid((20,1),(10,0),rowspan=5,colspan=1,sharex=ax1)
#ax1=plt.subplot(2,1,1)
#ax2=plt.subplot(2,1,2,sharex=ax1)
ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100ma'])
ax2.bar(df.index,df['Volume'])
plt.show()