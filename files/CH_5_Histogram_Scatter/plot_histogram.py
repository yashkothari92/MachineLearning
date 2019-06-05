import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

def test_run():
	start_date = '2014-05-31'
	end_date = '2019-05-31'

	dates = pd.date_range(start_date, end_date)

	# build empty data-frame
	df = pd.DataFrame(index=dates)

	# create data-frame for Ashok Leyland
	symbols = ['ASHOKLEY', 'TATAMOTORS']

	for symbol in symbols:
		dfy = pd.read_csv('../../stocks/{}.csv'.format(symbol), 
					index_col='Date',parse_dates = True, 
					usecols = ['Date', 'Adj Close'], na_values = ['nan'])
		
		dfy = dfy.rename(columns={'Adj Close':symbol})
		#print dfy
		df = df.join(dfy, how='inner')
	
		#data_plot(df, symbol)
		daily_returns = compute_daily_returns(df)
		#data_plot(df_daily_returns, 'Daily Returns')
	
		#Plot histogram	
		#df.hist()
		daily_returns.hist(bins=20, label=symbol)

		# Get mean & Standard Deviation
		mean = daily_returns[symbol].mean()
		print 'mean (',symbol,') =',mean

		std = daily_returns[symbol].std()
		print 'std =(',symbol,') =',std
		
		# plot mean, std
		plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
		plt.axvline(mean,color='w', linestyle= 'dashed', linewidth=2)
		plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
		plt.show()

		# Compute Kurtosis
		print 'kurtosis(',symbol,') =',daily_returns[symbol].kurtosis()	
	
	# Compute & plot both histograms on same chart
	daily_returns['ASHOKLEY'].hist(bins=20, label='ASHOKLEY')
	daily_returns['TATAMOTORS'].hist(bins=20, label='TATAMOTORS')
	plt.legend(loc='upper left')
	plt.show()


def compute_daily_returns(df):
	daily_returns = df.copy()
	daily_returns[1:]  = (daily_returns[1:]/daily_returns[:-1].values)-1
	daily_returns.ix[0,:] = 0
	return daily_returns

def data_plot(df, title):
	df.plot(title = title, label='StockLabel')
	plt.show()
	
if __name__ == "__main__":
	test_run()
