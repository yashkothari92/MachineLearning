import 	numpy as np

def test_run():
	# seed will help us to predict the random numbers, will stay the same everytimme we run it
	np.random.seed(121)
	a = np.random.randint(0, 10, size=(5,5))
	print a

	print "\nsum", a.sum()

	# -------Iterate over the rows to compute the sum--------
	print "\nColumn sum", a.sum(axis=0)

	
	# -------Iterate over the columns to compute the sum--------
	print "\nRow sum", a.sum(axis=1)

	# ---------Stastictics: min, max, avg, mean across rows and cols and overall--------
	print "\nMinimum of each column",  a.min(axis=0)
	print "\nMaximum of each row", a.max(axis=1)
	print "\nMean of all elements", a.mean()
	
	print "\nMax element at index", a.argmax()
	print "\nMax element at index", np.nanargmax(a, axis=0)

	# ----------Accesing array elements----------
	element = a[2,1]
	print "\nelement at (3,2)",element

	print "\nAll elements from col 0 till 5 (alternate) at every row"
	print a[:, 0:5:2]
	
	# -----------Modifying array elements----------
	print "\nModifying element at index (0,0)"
	a[0,0] = 19
	print a
	
	a[2, :] = [10, 20, 30, 40, 50]
	print a		

	# --------Indexing an array with another array--------
	a_new = np.random.randint(0, 10, size=20)
	print "\nNew array", a_new
	indices = np.array([1, 2, 8, 13])
	print "indexing at array",indices,"->",a_new[indices]

	# -------------"Mask" index array------------
	mean = a.mean()
	print "mean of a_new", mean
	a[a<mean] = mean
	print a
	
if __name__ == "__main__":
	test_run()
