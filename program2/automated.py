from hash_table import *
from stack import *
from queue import *
from time import time
import tracemalloc


def only_name():
	file = open('../files.txt', 'r')
	files = file.readlines()

	for i in range(len(files)):
		files[i] = files[i].replace('.txt\n', '')
	return files

def measure(func, file, *args):
	tracemalloc.start()
	first = int(time() * 1000)

	execute = func(*args)

	last = int(time() * 1000)
	_time = (last - first)
	print(f'{_time} milliseconds')

	current, peak = tracemalloc.get_traced_memory()
	tracemalloc.stop()
	peak = peak / (1024**2)
	print(f'Memory peak: {peak:.3} MB')
	f = open(file, "a")

	elements = 1
	if func.__name__[:5] == "_fill":
		elements = 10000
	elif func.__name__[-6:] == "search" :
		elements = 7

	f.write(f"{_time},{peak:.3},{elements}\n")
	f.close()


def show_files():
	print(only_name())

def fill_table():
	measure(_fill_table, "add_hash.txt")

def fill_stack():
	measure(_fill_stack, "add_stack.txt")

def fill_queue():
	measure(_fill_queue, "add_queue.txt")

def hash_search():
	measure(_hash_search, "search_hash.txt")

def stack_search():
	measure(_stack_search, "search_stack.txt")

def queue_search():
	measure(_queue_search, "search_queue.txt")

def add_hash(key, value):
	measure(_add_hash, "add_hash.txt", key, value)

def add_stack(element):
	measure(_add_stack, "add_stack.txt", element)

def add_queue(element):
	measure(_add_queue, "add_queue.txt", element)

def rm_stack():
	measure(_rm_stack, "remove_stack.txt")

def rm_queue():
	measure(_rm_queue, "remove_queue.txt")

def rm_hash(key):
	measure(_rm_hash, "remove_hash.txt", key)


def _fill_table():
	files = only_name()
	increase_table(len(files))
	set_all(files)
	print(f"Hash table filled with {len(files)} elements")


def _fill_stack():
	files = only_name()
	stacking_all(files)
	print(f"{len(files)} elements were stacked")

def _fill_queue():
	files = only_name()
	queuing_all(files)
	print(f"{len(files)} elements were queued")


def _hash_search():
	print("Searching for the 1th value.............")
	print(get_element('4cfda2fa45d445039a1b3f44018f5429'))
	print("Searching for the 100th value.............")
	print(get_element('24a59062c99a42d49698554f4eed2379'))
	print("Searching for the 1000th value.............")
	print(get_element('bf2982a8f37c47c79b42c70f42048af3'))
	print("Searching for the 5000th value.............")
	print(get_element('d48edae8085b4cb09e99b479b0456dd5'))
	print("Searching for the last three.............")
	print(get_element('a038cbbfd6014aaaa76e8c7d89179045'))
	print(get_element('902bbabf86c74bb49d4bee1c73cc7eef'))
	print(get_element('a3a6807dca8e4fe8b0e4d7ef91038faa'))

def _stack_search():
	print("Searching for the last three.............")
	print(unstacking())
	print(unstacking())
	print(unstacking())
	print("Searching for the 5000th element.............")
	print(unstacking_until(5000))
	print("Searching for the 1000th element.............")
	print(unstacking_until(1000))
	print("Searching for the 100th element.............")
	print(unstacking_until(100))
	print("Searching for the 1th element.............")
	print(unstacking_until(1))


def _queue_search():
	print("Searching for the 1th element.............")
	print(dequeuing_until(1))
	print("Searching for the 100th element.............")
	print(dequeuing_until(100))
	print("Searching for the 1000th element.............")
	print(dequeuing_until(1000))
	print("Searching for the 5000th element.............")
	print(dequeuing_until(5000))
	print("Searching for the last three elements.............")
	print(dequeuing_until(3897))
	print(dequeuing_until(1))
	print(dequeuing_until(1))


def _add_queue(element):
	print(queuing(element))

def _rm_queue():
	print(dequeuing())

def _add_stack(element):
	print(stacking(element))

def _rm_stack():
	print(unstacking())

def _add_hash(key, value):
	print(set_element(key, value))

def _rm_hash(key):
	print(remove_element(key))

