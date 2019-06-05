import pandas as pd

def test_run():
	df = pd.read_csv("../stocks/PAGEIND.csv")
	print df[445:453]

if __name__ == "__main__":
	test_run()
