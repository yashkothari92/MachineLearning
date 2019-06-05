import pandas as pd

def test_check():
	custom_dates = pd.date_range('2019-05-11', '2019-05-31')
	df = pd.DataFrame(index=custom_dates)

	df1 = pd.read_csv('../../stocks/TATAMOTORS.csv', index_col = 'Date', parse_dates = True, na_values=['nan'], usecols= ['Date','Adj Close', 'Volume'])
	df = df.join(df1)
	print df[1:]
	print ('--------------><-------------')
	print df[1:]/ df[:-1]
	
if __name__ == "__main__":
	test_check()
