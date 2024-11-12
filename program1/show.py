from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from execution_time import *

def only_name():
        file = open('../files.txt', 'r')
        files = file.readlines()
        for i in range(len(files)):
                files[i] = files[i].replace('.txt\n', '')

        return files

files = only_name()

def show(sorting_algorithm):
	match(sorting_algorithm):
		case 'unordered':
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
			print("Bubble Sort")
			bubble_time(files)
		case 'insertion':
			print("Insertion Sort")
			insertion_time(files)
		case 'selection':
			print("Selection Sort")
			selection_time(files)

