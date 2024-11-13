from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from execution_time import *
from random import randrange

def only_name():
	file = open('../files.txt', 'r')
	files = file.readlines()
	for i in range(len(files)):
		files[i] = files[i].replace('.txt\n', '')
	return files

def shuffle(list):
	for i in range(len(list)):
		r = randrange(0, len(list))
		memory = list[i]
		list[i] = list[r]
		list[r] = memory

def erase_data():
	open('bubble_time.txt', 'w').close()
	open('insertion_time.txt', 'w').close()
	open('selection_time.txt', 'w').close()
	print('The data has been deleted')



files = only_name()


def show(sorting_algorithm):
	match(sorting_algorithm):
		case 'unordered':
			print("Shuffling the list...")
			shuffle(files)
			print(files)
		case 'bubble':
			print(bubble_sort(files))
		case 'insertion':
			print(insertion_sort(files))
		case 'selection':
			print(selection_sort(files))


def time(sorting_algorithm):
	match(sorting_algorithm):
		case 'bubble':
			print("Shuffling the list...")
			shuffle(files)
			print("Bubble Sort")
			bubble_time(files)
		case 'insertion':
			print("Shuffling the list...")
			shuffle(files)
			print("Insertion Sort")
			insertion_time(files)
		case 'selection':
			print("Shuffiling the list...")
			shuffle(files)
			print("Selection Sort")
			selection_time(files)
		case _:
			print("Failed to start algorithm")


def shuffle_algorithms():
	algorithms = ['insertion', 'bubble', 'selection']
	shuffle(algorithms)
	for algorithm in algorithms:
		time(algorithm)

