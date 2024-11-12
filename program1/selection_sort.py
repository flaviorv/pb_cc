from bubble_sort import change

def selection_sort(list):
	for i in range(len(list)):
		indexof_smallest = i
		for j in range(i+1, len(list)):
			if list[indexof_smallest] > list[j]:
				indexof_smallest = j
		change(indexof_smallest, i, list)
	return list
