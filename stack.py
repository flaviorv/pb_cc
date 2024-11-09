from tp1 import only_name

files = only_name()

stack = []

def stacking(element):
	stack.append(element)

def unstacking():
	if len(stack) > 0:
		element = stack[len(stack)-1]
		del stack[len(stack)-1]
		return element
	return "There is nothing stacked"


def find(position_number):
	for i in range(len(stack)-1, -1, -1):
		element = stack[i][-32:]
		if i+1 == position_number:
			return "Element found in position " + str(i+1) + " = " + element
	return "Cannot find element in the position " + str(position_number)


def stacking_files():
	count = 0
	for file in files:
		count += 1
		stacking("Number " + str(count) + " in the stack = " + file)


stacking_files()
print(unstacking())
print(unstacking())
print(unstacking())
print(find(6700))
print(find(10000))
print(find(1))
print(find(0))
print(find(10001))
