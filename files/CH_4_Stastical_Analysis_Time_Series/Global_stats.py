import pandas as pd
import matplotlib.pyplot as plt

########
##### See plot_selected function to see 
######Global stats, Rolling mean stats & Daily returns

def test_run():
	start_date = '2019-01-01'
        end_date = '2019-05-31'
  
        dates = pd.date_range(start_date, end_date)
  
        # Create an empty data-frame
	df1 = pd.DataFrame(index=dates)
	# create data-frame for Ashok Leyland
	'''
	dfEICHER = pd.read_csv('../stocks/EICHERMOT.csv', 
				index_col='Date', 
				parse_dates = True, usecols=['Date', 'Adj Close'],
				na_values=['nan'])

	# Rename Adj Close column to EICHER to prevent clash	
	dfEICHER = dfEICHER.rename(columns={'Adj Close': 'EICHER'})
	
	# join two data-frames using DataFrame.join
	df1=df1.join(dfEICHER, how='inner')
	
	# Drop NaN values
	df1 = df1.dropna()'''

#	print df1

#	symbols = ['ASHOKLEY', 'TATAMOTORS', 'MARUTI', 'HEROMOTOCO']
	symbols = ['ASHOKLEY']
	for symbol in symbols:
		df_temp = pd.read_csv('../../stocks/{}.csv'.format(symbol), index_col='Date',
				parse_dates = True, 
				usecols = ['Date' , 'Adj Close'],
				na_values = ['nan'])
		
		df_temp = df_temp.rename(columns={'Adj Close': symbol})
		df1 = df1.join(df_temp, how='inner')
#		df1 = df1/df1.ix[0]

	print df1
	
	# slice and plot
	plot_selected(df1, symbols, start_date, end_date)



def plot_selected(df, columns, start_index, end_index):
	df1 = df.ix[start_index:end_index, columns]
	ax = df1.plot(title="AL Rolling Mean", label='Ashok Leyland')
	plt.show()

	#----------- Compute Global statistics for each stock ----------
	print "\nMean\n", df.mean()
	print "\nMedian\n",df.median()
	print "\nStd\n", df.std()
	
	# ------------- Compute Rolling statistics ---------------
	rm_al = pd.rolling_mean(df, window=20)
	rm_std_al = pd.rolling_std(df, window=20)
	
	upper_band = rm_al + rm_std_al*2
	lower_band = rm_al - rm_std_al*2
	
	rm_al.plot(label='Rolling mean', ax=ax)
	upper_band.plot(label='UpperBand', ax=ax)
	lower_band.plot(label='LowerBand', ax=ax)
	
	# --------------Daily Returns ----------------
	daily_returns = df.copy()
	# dividing every row's price by previous day's price and subtract 1 from it
	daily_returns[1:] = (daily_returns[1:]/daily_returns[:-1].values) - 1
	# set daily returns for row 0 to 0
	daily_returns.ix[0, :] = 0	
	daily_returns.plot() 
	
	# -----------Cumulative Returns-----------
	cumul_returns = df.copy()

	cumul_returns =  ((cumul_returns.ix[-1]/cumul_returns.ix[0].values)-1)*100
	print "\nCumulative Returns in Year 2019 by Ashok Leyland is",cumul_returns
	plot_data(cumul_returns)	
	plt.show()
	plt.clf()

def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
     """Plot stock prices with a custom title and meaningful axis labels."""
     ax = df.plot(title=title, fontsize=12)
     ax.set_xlabel(xlabel)
     ax.set_ylabel(ylabel)
     plt.show()
	
if __name__ == "__main__":
	test_run()
