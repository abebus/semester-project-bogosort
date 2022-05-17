from time import perf_counter_ns
import csv
from bogosort_np_njit import *

path = 'dataset/data'

if __name__ == '__main__':
	sets = range(1)
	num_of_elems = range(1, 3)
	
	with open('res.csv', 'w', newline='') as write:
		write = csv.writer(write, delimiter='\t')
		write.writerow(['set#', 'elems-n', 'nanosec'])  # header
		for set_ in sets:
			for n in num_of_elems:
				with open(f'{path}/{set_}/{n}.csv', newline='') as read:
					arr = np.array(list(map(int, *(csv.reader(read, delimiter=';')))))
					print(arr)
					
					start = perf_counter_ns()
					bogosort(arr)
					finish = perf_counter_ns()
					print(arr)
					
					ns = finish - start
					print([set_, n, ns])
					write.writerow([set_, n, ns])
					