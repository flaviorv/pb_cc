import plotext as plt

def read(file):
	times = []
	peaks = []
	elements = []
	time = 0
	peak = 0
	element = 0
	f = open(file, 'r')
	lines = f.readlines()
	for line in lines:
		splited = line.split(",")
		time += float(splited[0])
		peak += float(splited[1])
		element += float(splited[2])
		times.append(time)
		peaks.append(peak)
		elements.append(element)

	data = [times, peaks, elements]
	return data


#type must search, rm or add
def graph(type):
	try:
		hash = read(f'{type}_hash.txt')
	except:
		hash = [[], [], []]
	try:
		queue = read(f'{type}_queue.txt')
	except:
		queue = [[], [], []]
	try:
		stack = read(f'{type}_stack.txt')
	except:
		stack = [[], [], []]
	if len(hash[2]) > 0 or len(stack[2]) > 0 or len(stack[2]) > 0:
		if len(hash[0]) > 0:
			plt.plot(hash[2], hash[0], color='red', label='Hash Table')
		if len(queue[0]) > 0:
			plt.plot(queue[2], queue[0], color='green', label='Queue')
		if len(stack[0]) > 0:
			plt.plot(stack[2], stack[0], color='blue', label='Stack')
		plt.title(f"{type.upper()} - Time")
		plt.ylabel("Milliseconds")
		plt.xlabel("Elements")
		plt.theme('dark')
		plt.show()
		plt.clf()
		print()
		if len(hash[1]) > 0:
			plt.plot(hash[2], hash[1], color='red', label='Hash Table')
		if len(queue[1]) > 0:
			plt.plot(queue[2], queue[1], color='green', label='Queue')
		if len(stack[1]) > 0:
			plt.plot(stack[2], stack[1], color='blue', label='Stack')
		plt.title(f"{type.upper()} - Memory Peak")
		plt.ylabel("MB")
		plt.xlabel("Elements")
		plt.theme('dark')
		plt.show()
		plt.clf()

	else:
		print('Unable to create charts - No data')




def erase_data():
	structures = ['hash', 'stack', 'queue']
	features = ['remove', 'add', 'search']
	for structure in structures:
		for feature in features:
			open(f'{feature}_{structure}.txt', 'w').close()
	print('The data has been deleted')
