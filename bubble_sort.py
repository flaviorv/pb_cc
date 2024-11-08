from time import time

def bubble_sort(list):
	before = int(time() * 1000)
	for i in range(len(list) -1):
		for j in range(i+1, len(list)):
			if list[i] > list[j]:
				change(i, j, list)
	after = int(time() * 1000)
	print(str(after - before), "milliseconds")
	return list

def change(index1, index2, list):
	memory = list[index1]
	list[index1] = list[index2]
	list[index2] = memory
