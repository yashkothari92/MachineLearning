import pandas as pd
import matplotlib.pyplot as plt

def test_run():
	df = pd.read_csv("../stocks/PAGEIND.csv")
	print df['Adj Close']
	df[['High', 'Low']].plot()

	plt.xlabel('Time')
	plt.ylabel('Price')
	plt.title('PAGE IND stock chart')
	plt.show()

if __name__ == "__main__":
	test_run()
