import pandas as pd

def test_run():
	start_date = '2018-01-21'
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

	symbols = ['ASHOKLEY', 'TATAMOTORS']

	for symbol in symbols:
		df_temp = pd.read_csv('../stocks/{}.csv'.format(symbol), index_col='Date',
				parse_dates = True, 
				usecols = ['Date' , 'Adj Close'],
				na_values = ['nan'])

		
		df_temp = df_temp.rename(columns={'Adj Close': symbol})
		df1 = df1.join(df_temp, how='inner')

	print df1

if __name__ == "__main__":
	test_run()
