import csv
import os
from numpy import random as r

names_of_sets = [f'{i}' for i in range(100)]
number_of_elements_list = [_ for _ in range(1, 12)]
border = 1000

path_to_dataset = os.path.join(os.getcwd(), "data")
for set_ in names_of_sets:
	path_to_set = os.path.join(path_to_dataset, set_)
	try:
		os.mkdir(path_to_set)
	except OSError:
		pass
	
	for number_of_elements in number_of_elements_list:
		path_to_file = os.path.join(path_to_set, str(number_of_elements) + '.csv')
		data = []
		for _ in range(number_of_elements):
			data.append(r.randint(-border, border))
		
		with open(path_to_file, "w", newline='') as file:
			writer = csv.writer(file, delimiter=';')
			writer.writerow(data)

