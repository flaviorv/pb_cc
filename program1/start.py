from show import *

option = ''
while option != 'exit':
	print('============== SORTING ALGORITHMS ==============')
	print('Type 1 to show unordered list')
	print('Type 2 to show ordered list for bubble sort')
	print('Type 3 to show ordered list for insertion sort')
	print('Type 4 to show ordered list for selection sort')
	print('Type 5 to execution time for bubble sort')
	print('Type 6 to execution time for insertion sort')
	print('Type 7 to execution time for selection sort')
	print('Type 0 to exit')
	option = input()
	match(option):
		case '1':
			show('unordered')
		case '2':
			show('bubble')
		case '3':
			show('insertion')
		case '4':
			show('selection')
		case '5':
			time('bubble')
		case '6':
			time('insertion')
		case '7':
			time('selection')
		case '0':
			print('Exiting the application')
			option = 'exit'
		case _:
			print('Invalid command')
