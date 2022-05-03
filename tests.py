from time import perf_counter_ns
import csv

# import numpy as np
from bogosort_np_njit import *

path = 'dataset/data'

if __name__ == '__main__':
	sets = range(1)
	num_of_elems = range(3, 4)
	
	timings = []
	for set_ in sets:
		for n in num_of_elems:
			with open(f'{path}/{set_}/{n}.csv', newline='') as file:
				arr = np.array(list(map(int, *(csv.reader(file, delimiter=';')))))
				
				start = perf_counter_ns()
				bogosort(arr)
				finish = perf_counter_ns()
				
				ns = finish - start
				timings.append([set_, n, ns])
				
	with open('res.csv', 'w', newline='') as file:
		res = csv.writer(file, delimiter='\t')
		res.writerow(['set', 'n', 'ns'])  # header
		res.writerows(timings)
		