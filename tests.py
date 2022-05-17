from time import perf_counter_ns
import csv
from bogosort_np_njit import *

path = 'dataset/data'

if __name__ == '__main__':
	sets = range(100)
	num_of_elems = range(1, 12)
	
	with open('res.csv', 'w', newline='') as write:
		write = csv.writer(write, delimiter='\t')
		write.writerow(['set#', 'elems-n', 'nanosec'])  # header
		for set_ in sets:
			for n in num_of_elems:
				with open(f'{path}/{set_}/{n}.csv', newline='') as read:
					arr = np.array(list(map(int, *(csv.reader(read, delimiter=';')))))
					
					start = perf_counter_ns()
					bogosort(arr)
					finish = perf_counter_ns()
					
					ns = finish - start
					write.writerow([set_, n, ns])
					