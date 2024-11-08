from bubble_sort import change
from time import time

def selection_sort(list):
	before = int(time() * 1000)
	for i in range(len(list)):
		indexof_smallest = i
		for j in range(i+1, len(list)):
			if list[indexof_smallest] > list[j]:
				indexof_smallest = j
		change(indexof_smallest, i, list)

	after = int(time() * 1000)
	print(str(after - before), "milliseconds")
	return list
