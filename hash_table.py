from tp1 import only_name
from test import test_list
from hashlib import sha256

files = only_name()

table = [[] for _ in range(len(files))]

def find_index(key):
	global table
	length = len(table)
	try:
		return int(sha256(key.encode()).hexdigest(), 16) % length
	except:
		print("This key is not hashable. key should be a string")

def set_element(key, value):
	global table
	index = find_index(str(key))
	element = [key, value]
	table[index].append(element)


def get_element(key):
	global table
	index = find_index(key)
	#in case of conflict there is more than one element
	elements = table[index]
	for element in table[index]:
                _key = element[0]
                _value = element[1]
                if _key == key:
                        print(_value)
                        return _value
	print("Element not found")


def hash_files():
        for file in files:
                key = file
                value = "Value of " + file
                set_element(key, value)


hash_files()
get_element('14f7b68bef6f44b89bfcbb289edcb203')
get_element('22a5676fe1a349e292f5c7c877becc1c')
get_element('Non-existent key')
