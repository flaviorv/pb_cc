from tp1 import only_name

files = only_name()

queue = []

def queuing(element):
	element = str(element)
	queue.append(element)

def dequeuing():
	if len(queue) > 0:
		first = queue[0]
		del queue[0]
		return first
	return "Queue is empty"

def find(position_number):
	for i in range(len(queue)):
		if (i+1) == position_number:
			element = queue[i]
			element = element[-32:]
			return "Element found in position " + str(i+1) + " = " + element
	return "Cannot found element in the position " + str(position_number)

def enqueuing_files():
	count = 0
	for file in files:
		count += 1
		queuing("Number " +  str(count) + " in the queue = " +  file)


enqueuing_files()
print(find(6700))
print(find(10000))
print(find(1))
print(find(0))
print(find(10001))
print(dequeuing())
print(dequeuing())
print(dequeuing())
