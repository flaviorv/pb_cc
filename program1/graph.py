import plotext as plt

b_times = []
b_elements = []

def b_read():
	time = 0
	elements = 0
	file = open("bubble_time.txt", "r")
	file = file.readlines()
	for line in file:
		splited = line.split(",")
		time += int(splited[0])
		elements += int(splited[1])
		b_times.append(time)
		b_elements.append(elements)


i_times = []
i_elements = []

def i_read():
	time = 0
	elements = 0
	file = open("insertion_time.txt", "r")
	file = file.readlines()
	for line in file:
		splited = line.split(",")
		time += int(splited[0])
		elements += int(splited[1])
		i_times.append(time)
		i_elements.append(elements)

s_times = []
s_elements = []

def s_read():
	time = 0
	elements = 0
	file = open("selection_time.txt", "r")
	file = file.readlines()
	for line in file:
		splited = line.split(",")
		time += int(splited[0])
		elements += int(splited[1])
		s_times.append(time)
		s_elements.append(elements)


def graph():
	b_read()
	i_read()
	s_read()
	if len(b_times) > 0 or len(s_elements) > 0 or len(i_elements):
		if len(b_times) > 0 and len(b_elements) > 0:
			plt.plot(b_elements, b_times, color="red", label="Bubble Sort")
		if len(i_times) > 0 and len(i_elements) > 0:
			plt.plot(i_elements, i_times, color="green", label="Insertion Sort")
		if len(s_times) > 0 and len(s_elements) > 0:
			plt.plot(s_elements, s_times, color="blue", label ="Selection Sort")
		plt.title("Execution Time")
		plt.ylabel("Milliseconds")
		plt.xlabel("Sorted Elements")
		plt.theme("dark")
		plt.show()
		plt.clf()
	else:
		print("No data - Graphics are generated after sorting lists")
