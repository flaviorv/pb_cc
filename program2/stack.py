stack = []

def stacking(element):
	stack.append(element)
	return f"{element} is stacked.\nStack has now {len(stack)} elements"

def unstacking():
	if len(stack) > 0:
		element = stack[len(stack)-1]
		del stack[len(stack)-1]
		return f"Found: {element}\nStack has now {len(stack)} elements"
	return "There is nothing stacked"


def unstacking_until(position_number):
	if position_number > len(stack):
		return f"Cannot find element in the position {position_number}"
	times = len(stack) - position_number + 1
	for i in range(times):
		if i+1 == times:
			print(f"{times} elements unstacked")
			return unstacking()
		else:
			unstacking()


def stacking_all(list):
	count = 0
	for element in list:
		count += 1
		stacking(f"Number {count} in the stack = {element}")


def show_stack():
	print(stack)
