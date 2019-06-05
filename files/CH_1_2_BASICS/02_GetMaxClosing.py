import pandas as pd

def get_max_close(symbol):
	df = pd.read_csv("../stocks/{}.csv".format(symbol))
	print df['Volume'].mean()
	return df['Close'].max()


def test_run():
	for symbol in ['EICHERMOT', 'PAGEIND']:
		print "Max Close:"
		print symbol, get_max_close(symbol)

if __name__ == "__main__":
	test_run()
