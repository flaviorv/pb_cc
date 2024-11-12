from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from time import time

def bubble_time(list):
	first = int(time() * 1000)
	bubble_sort(list)
	last = int(time() * 1000)
	_time = (last-first)
	print(f"Execution Time: {_time} milliseconds")

def insertion_time(list):
	first = int(time() * 1000)
	insertion_sort(list)
	last = int(time() * 1000)
	_time = (last-first)
	print(f"Execution Time: {_time} milliseconds")

def selection_time(list):
	first = int(time() * 1000)
	selection_sort(list)
	last = int(time() * 1000)
	_time = (last-first)
	print(f"Execution Time: {_time} milliseconds")
