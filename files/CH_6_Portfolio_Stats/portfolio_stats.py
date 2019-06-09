import pandas as pd
import numpy as np

def test_run():

	start_date = '2018/05/01'
	end_date = '2019/05/31'

	dates = pd.date_range(start_date, end_date)
	symbols = ['MARUTI', 'HDFCBANK', 'TATAMOTORS', 'PCJEWELLER']
	# Get Data
	df = get_data(symbols, dates)

def daily_avg_return(df):
	print "Average daily returns:",np.sum(df[1:].values/df[:-1].values)/len(df)
	
def daily_return(df):
	return (df[1:]/df[:-1].values)-1

def cumulative_return(df):
	#print "df[-1:]\n",df[-1:]
	#print "df[:1] \n",df[:1]
	return ((df[-1:].values - df[:1].values)/df[:1].values)*100
	
def get_data(symbols, dates):
	df = pd.DataFrame(index=dates)

	for symbol in symbols:
		df1 = pd.read_csv('../../stocks/{}.csv'.format(symbol),
				index_col='Date', parse_dates=True, 
				na_values= ['nan'], 
				usecols=['Date','Adj Close'])
		
		print ">>", symbol
		df = df.join(df1, how='inner')
		df = df.rename(columns={'Adj Close': symbol})
		df.dropna()
		
		# Get Cumulative Return
		cum_return = cumulative_return(df[symbol])
		print "Cumulative return \t", cum_return
		
		# Get avg daily return
		daily_avg_return(df[symbol])

		# Standard Deviation of daily return
		df_daily_ret = daily_return(df[symbol])
		print "Std ",df_daily_ret.std()	
		
		# Sharpe Ratio
		# Gather daily returns(a) & risk free rate of return(b) , take the mean of a-b; Std Deviation of daily returns
		print "sharpe ratio  ",(df_daily_ret.mean()/df_daily_ret.std())*np.sqrt(len(df_daily_ret))
		
		
		print "\n"
	return df

if __name__ == "__main__":
	test_run()
