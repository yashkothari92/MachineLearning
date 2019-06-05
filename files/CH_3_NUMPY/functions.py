import numpy as np

def test_run():
	# List to 1D array
	print('Simply printing 1D array')
	print np.array([2,3,4])

	#List of tuples to 3D arry
	print('\ntuple of 2D array of 3cols & 3rows')
	print np.array([(1,2,3),(4,5,6),(7,8,9)])

	# Empty array with init value
	print('\nEmpty array with 5 rows & 3 cols')
	print np.empty((5, 3))
	
	# Array of 1s
	print('\nArray of 1s')
	print np.ones((3,2))
	
	print('\nArray of 1s with type Integer')
	print np.ones((3,3), dtype=int)

	print('\nGenerating random numbers')
	# universal sampling of random numbers from [0.0, 1.0)
	print np.random.random((1,1))

	print('\nRandom nos generated in custom range (default mean = 0, s.d=1)')
	# Sample numbers from a Gaussian (normal) distribution 
	print np.random.normal(size=(2,3)) # "standard normal" (mean = 0, s.d = 1)
	
	print('\nRandom nos generated in range: mean = 90 & s.d = 10')
	print np.random.normal(90, 10, size=(2,2)) # (mean = 90, s.d = 10)

	print('\nrandInt function demonstration')
	print np.random.randint(10)
	print np.random.randint(0, 10)
	print np.random.randint(0,10, size=5)
	print np.random.randint(0, 10, size=(2,4))

	print('\nArray attributes')	
	a = np.random.normal(size=(2,3)) # "standard normal" (mean = 0, s.d = 1)
	print a
	print "shape", a.shape
	print "length of shape ",len(a.shape)
	print "dtype ", a.dtype
	print "size",a.size
	print "1st element of shape",a.shape[0]  
	
if __name__ == "__main__":
	test_run()
