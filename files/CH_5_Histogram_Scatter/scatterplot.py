import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
beta_TM= 1.6015284568156742
alpha_TM= -0.001464810627364336

beta_AL= 1.2161667528646114
alpha_AL= -0.00041152652475163006

beta_REL= 1.050787902404099
alpha_REL= 0.0008753309026685705

beta_HDFC= 0.7316307134793208
alpha_HDFC= 0.0006089025515227293

Higher beta-value, stock is more reactive to market (i.e.Nifty)
(For eg,Tata Motors is more reactive to Nifty50 than any other stock; and HDFC is least reactive stock w.r.t to Nifty50)

Alpha value denotes how well the stock performes with respect to Nifty
(For eg, Reliance performs well w.r.t to Nifty50, whereas TataMotors performs worst w.r.t to Nifty50)

                NSEI  ASHOKLEY  TATAMOTORS  RELIANCE  HDFCBANK
NSEI        1.000000  0.443935    0.572909  0.534623  0.601598
ASHOKLEY    0.443935  1.000000    0.388016  0.258503  0.203668
TATAMOTORS  0.572909  0.388016    1.000000  0.293186  0.249989
RELIANCE    0.534623  0.258503    0.293186  1.000000  0.261324
HDFCBANK    0.601598  0.203668    0.249989  0.261324  1.000000

Based on above result on correlation, we can say that NSE and HDFC BK are highly correlated, whereas value of NSE & AshokLey is very small.

'''

def test_run():

	# Read data
	start_date = '2016-01-01'
	end_date = '2019-01-31'
	dates = pd.date_range(start_date, end_date)

	symbols = ['NSEI','ASHOKLEY', 'TATAMOTORS', 'RELIANCE', 'HDFCBANK']
	df = get_data(symbols, dates)

	# Compute Daily returns
	daily_returns = compute_daily_returns(df)
	print daily_returns
	
	# Scatter plot (NSE Vs TATA Motors)
	daily_returns.plot(kind='scatter', x = 'NSEI', y = 'TATAMOTORS')
	# beta: polyomial co-efficient, alpha: intercept (y=mx+b); m=co-efficient: beta, b=intercept: alpha

	beta_TM, alpha_TM = np.polyfit(daily_returns['NSEI'], daily_returns['TATAMOTORS'], 1)	# 1 denotes degree of a function
	print 'beta_TM=',beta_TM
	print 'alpha_TM=',alpha_TM

	plt.plot(daily_returns['NSEI'],beta_TM*daily_returns['NSEI']+alpha_TM, '-', color='r') # '-' denotes that desired one is line plot 
	plt.show()

	# Scatter plot (NSE Vs Ashok Leyland)
	daily_returns.plot(kind='scatter', x = 'NSEI', y = 'ASHOKLEY')
	beta_AL, alpha_AL = np.polyfit(daily_returns['NSEI'], daily_returns['ASHOKLEY'],1)	
	print 'beta_AL=',beta_AL
	print 'alpha_AL=',alpha_AL

	plt.plot(daily_returns['NSEI'],beta_AL*daily_returns['NSEI']+alpha_AL, '-', color='r') # '-' denotes that desired one is line plot 
	plt.show()

	# Scatter plot (NSE Vs Reliance)
	daily_returns.plot(kind='scatter', x = 'NSEI', y = 'RELIANCE')
	# beta: polyomial co-efficient, alpha: intercept (y=mx+b); m=co-efficient: beta, b=intercept: alpha

	beta_REL, alpha_REL = np.polyfit(daily_returns['NSEI'], daily_returns['RELIANCE'], 1)	# 1 denotes degree of a function
	print 'beta_REL=',beta_REL
	print 'alpha_REL=',alpha_REL

	plt.plot(daily_returns['NSEI'],beta_REL*daily_returns['NSEI']+alpha_REL, '-', color='r') # '-' denotes that desired one is line plot 
	plt.show()

	# Scatter plot (NSE Vs HDFC Bank )
	daily_returns.plot(kind='scatter', x = 'NSEI', y = 'HDFCBANK')
	beta_HDFC, alpha_HDFC = np.polyfit(daily_returns['NSEI'], daily_returns['HDFCBANK'],1)	
	print 'beta_HDFC=',beta_HDFC
	print 'alpha_HDFC=',alpha_HDFC

	plt.plot(daily_returns['NSEI'],beta_HDFC*daily_returns['NSEI']+alpha_HDFC, '-', color='r') # '-' denotes that desired one is line plot 
	plt.show()

	print daily_returns.corr(method='pearson')	

def get_data(symbols, dates):
	
	# build empty data-frame
	df = pd.DataFrame(index=dates)

	# create data-frame for Ashok Leyland

	for symbol in symbols:
		dfy = pd.read_csv('../../stocks/{}.csv'.format(symbol), 
					index_col='Date',parse_dates = True, 
					usecols = ['Date','Adj Close'], na_values = ['nan'])
	 	
		dfy = dfy.dropna()	
		dfy = dfy.rename(columns={'Adj Close':symbol})
		#print dfy
		df = df.join(dfy, how='inner')
	
	return df

def compute_daily_returns(df):
	daily_returns = df.copy()
	daily_returns[1:]  = (daily_returns[1:]/daily_returns[:-1].values)-1
	daily_returns.ix[0,:] = 0
	return daily_returns

def data_plot(df, title):
	df.plot(title = title, label='StockLabel')
	plt.show()

'''	
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
		plt.axvline(mean,color='w', linestyle= 'dashed', linewidth=2)
		plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
		plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
		plt.show()

		# Compute Kurtosis
		print 'kurtosis(',symbol,') =',daily_returns[symbol].kurtosis()	
	
	# Compute & plot both histograms on same chart
	daily_returns['ASHOKLEY'].hist(bins=20, label='ASHOKLEY')
	daily_returns['TATAMOTORS'].hist(bins=20, label='TATAMOTORS')
	plt.legend(loc='upper left')
	plt.show()

	data_plot(df, symbol)'''

if __name__ == '__main__':
	test_run()
