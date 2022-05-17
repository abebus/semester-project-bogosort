import numpy as np
from numba import njit


@njit("void(int32[:])", fastmath=True)
def bogosort(bogo):
	is_sorted = False
	size = len(bogo)
	if size < 2:
		return
	while not is_sorted:
		np.random.shuffle(bogo)
		for i in np.arange(size - 1):
			if bogo[i] <= bogo[i + 1]:
				is_sorted = True
			else:
				is_sorted = False
				break
				