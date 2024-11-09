from random import randrange
def test_list(length):
	list = []
	for _ in range(length):
		number = randrange(0, 50)
		list.append(number)
	return list
