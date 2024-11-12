def bubble_sort(list):
	for i in range(len(list) -1):
		for j in range(i+1, len(list)):
			if list[i] > list[j]:
				change(i, j, list)
	return list

def change(index1, index2, list):
	memory = list[index1]
	list[index1] = list[index2]
	list[index2] = memory
