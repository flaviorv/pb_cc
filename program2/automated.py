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


def show_files():
	tracemalloc.start()
	first = int(time() * 1000)

	print(only_name())

	last = int(time() * 1000)
	_time = (last - first)
	print(f'{_time} milliseconds')

	current, peak = tracemalloc.get_traced_memory()
	print(f"Memory peak: {peak / 10**6} MB")
	tracemalloc.stop()


def fill_table():
	tracemalloc.start()
	first = int(time() * 1000)

	files = only_name()
	increase_table(len(files))
	set_all(files)
	print(f"Hash table filled with {len(files)} elements")

	last = int(time() * 1000)
	_time = (last-first)
	print(f"{_time} milliseconds")

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()

def fill_stack():
	tracemalloc.start()
	first = int(time() * 1000)

	files = only_name()
	stacking_all(files)
	print(f"{len(files)} elements were stacked")
	last = int(time() * 1000)
	_time = (last-first)
	print(f"{_time} milliseconds")

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()

def fill_queue():
	tracemalloc.start()
	first = int(time() * 1000)

	files = only_name()
	queuing_all(files)
	print(f"{len(files)} elements were queued")

	last = int(time() * 1000)
	_time = (last-first)
	print(f"{_time} milliseconds")

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()

def hash_search():
	tracemalloc.start()
	first = int(time() * 1000)

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

	last = int(time() * 1000)
	_time = (last-first)
	print(f"{_time} milliseconds")

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6}')
	tracemalloc.stop()

def stack_search():
	tracemalloc.start()
	first = int(time() * 1000)

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

	last = int(time() * 1000)
	_time = (last - first)
	print(f"{_time} milliseconds")

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak = {peak / 10**6} MB')
	tracemalloc.stop()

def queue_search():
	tracemalloc.start()
	first = int(time() * 1000)

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

	last = int(time() * 1000)
	_time = (last - first)
	print(f"{_time} milliseconds")

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak = {peak / 10**6} MB')
	tracemalloc.stop()

def add_queue(element):
	tracemalloc.start()
	first = int(time() * 1000)

	print(queuing(element))

	last = int(time() * 1000)
	_time = (last - first)
	print(f'{_time} milliseconds')

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()


def rm_queue():
	tracemalloc.start()
	first = int(time() * 1000)

	print(dequeuing())

	last = int(time() * 1000)
	_time = (last - first)
	print(f'{_time} milliseconds')

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()


def add_stack(element):
	tracemalloc.start()
	first = int(time() * 1000)

	print(stacking(element))

	last = int(time() * 1000)
	_time = (last - first)
	print(f'{_time} milliseconds')

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()


def rm_stack():
	tracemalloc.start()
	first = int(time() * 1000)

	print(unstacking())

	last = int(time() * 1000)
	_time = (last - first)
	print(f'{_time} milliseconds')

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()


def add_hash(key, value):
	tracemalloc.start()
	first = int(time() * 1000)

	print(set_element(key, value))

	last = int(time() * 1000)
	_time = (last - first)
	print(f'{_time} milliseconds')

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()


def rm_hash(key):
	tracemalloc.start()
	first = int(time() * 1000)

	print(remove_element(key))

	last = int(time() * 1000)
	_time = (last - first)
	print(f'{_time} milliseconds')

	current, peak = tracemalloc.get_traced_memory()
	print(f'Memory peak: {peak / 10**6} MB')
	tracemalloc.stop()
