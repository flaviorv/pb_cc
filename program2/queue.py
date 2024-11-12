queue = []

def queuing(element):
	queue.append(element)
	return f"{element} queued"

def dequeuing():
	if len(queue) > 0:
		first = queue[0]
		del queue[0]
		return f"Found: {first}\nQueue has now {len(queue)} elements"
	return "Queue is empty"

def dequeuing_until(position_number):
	if position_number > len(queue):
		return f"Cannot find element in the position {position_number}\nQueue has {len(queue)} elements"
	count = 0
	for i in range(1, position_number+1):
		if i == position_number:
			count += 1
			print(f"{count} elements dequeued")
			return dequeuing()
		else:
			count += 1
			dequeuing()

def queuing_all(list):
	count = 0
	for element in list:
		count += 1
		queuing(f"Number {count} in the queue = {element}")


def show_queue():
	print(queue)

