import pandas as pd


def test_run():
	# Define date range
	start_date = '2018-01-21'
	end_date = '2019-05-31'
	
	dates = pd.date_range(start_date, end_date)
	#print dates[3]

	# Create an empty data-frame
	df1 = pd.DataFrame(index=dates)
	print df1

if __name__ == "__main__":
	test_run()
