from time import time

def insertion_sort(list):
	before = int(time() * 1000)
	for i in range(1, len(list)):
		current = list[i]
		for j in range(i -1, -2, -1 ):
			previous = list[j]
			if j >= 0 and previous > current:
				list[j+1] = previous
			else:
				list[j+1] = current
				break
	after = int(time() * 1000)
	print(str(after - before), "milliseconds")
	return list

