import pandas_datareader.data as web
import datetime 
import matplotlib.pyplot as plt


start=datetime.date(2010,1,1)
end=datetime.date(2018,6,22)

print(start)

tickers=['GE']

df=web.DataReader(tickers[0],'morningstar',start,end)

print(df.tail())

print(df.describe())


df['Close'].plot(title='GE Stock')

df.to_csv(tickers[0]+'.csv')
plt.show()