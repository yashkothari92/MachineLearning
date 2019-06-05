import pandas as pd
import matplotlib.pyplot as plt

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

	symbols = ['ASHOKLEY', 'TATAMOTORS', 'MARUTI', 'HEROMOTOCO']

	for symbol in symbols:
		df_temp = pd.read_csv('../stocks/{}.csv'.format(symbol), index_col='Date',
				parse_dates = True, 
				usecols = ['Date' , 'Adj Close'],
				na_values = ['nan'])
		
		df_temp = df_temp.rename(columns={'Adj Close': symbol})
		df1 = df1.join(df_temp, how='inner')
		df1 = df1/df1.ix[0]

	print df1
	
	# slice and plot
	plot_selected(df1, symbols, start_date, end_date)



def plot_selected(df, columns, start_index, end_index):
	df = df.ix[start_index:end_index, columns]
	df.plot()

	plt.title("Stock")
	plt.xlabel("Time")
	plt.ylabel("Price")
	
	plt.show()


if __name__ == "__main__":
	test_run()
