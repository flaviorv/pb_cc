from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from time import time

def bubble_time(list):
	first = int(time() * 1000)
	b = bubble_sort(list)
	last = int(time() * 1000)
	_time = (last-first)
	print(f"Execution Time: {_time} milliseconds")
	f = open("bubble_time.txt", "a")
	f.write(f"{_time},{len(b)}\n")
	f.close()

def insertion_time(list):
	first = int(time() * 1000)
	i = insertion_sort(list)
	last = int(time() * 1000)
	_time = (last-first)
	print(f"Execution Time: {_time} milliseconds")
	f = open("insertion_time.txt", "a")
	f.write(f"{_time},{len(i)}\n")
	f.close()

def selection_time(list):
	first = int(time() * 1000)
	s = selection_sort(list)
	last = int(time() * 1000)
	_time = (last-first)
	print(f"Execution Time: {_time} milliseconds")
	f = open("selection_time.txt", "a")
	f.write(f"{_time},{len(s)}\n")
	f.close()
