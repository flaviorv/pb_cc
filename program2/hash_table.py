from hashlib import sha256

table = [[] for _ in range(20)]

def show_table():
	print(table)

def increase_table(length):
	global table
	table = [[] for _ in range(length)]


def find_index(key):
	length = len(table)
	try:
		return int(sha256(key.encode()).hexdigest(), 16) % length
	except:
		print("This key is not hashable. key should be a string")

def set_element(key, value):
	index = find_index(str(key))
	element = [key, value]
	table[index].append(element)
	return 'Element added'


def get_element(key):
	index = find_index(key)
	#in case of colisions there is more than one element
	for element in table[index]:
                _key = element[0]
                _value = element[1]
                if _key == key:
                        return f"Found: {_value}"
	return "Element not found"


def remove_element(key):
	index = find_index(key)
	for i, element in enumerate(table[index]):
		_key = element[0]
		if _key == key:
			del table[index][i]
			return 'Element removed'
	return 'Element not found'


def set_all(list):
        for i in range(len(list)):
                key = list[i]
                value = f"Value of {list[i]}"
                set_element(key, value)


def all_keys():
	count =0
	for index_elements in table:
		for j in index_elements:
			count += 1
			print(f"key {count} {j[0]}")
