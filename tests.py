from time import perf_counter_ns
import numpy as np
import csv
from bogosort_np_njit import bogosort

path = 'dataset/data'


def time_it(f):
	def wrapper(*args):
		start = perf_counter_ns()
		f(*args)
		finish = perf_counter_ns()
		return finish - start
	return wrapper


if __name__ == '__main__':
	
	with open('res.csv', 'w', newline='') as res:
		csv.writer(res, delimiter='\t')
		pass
		