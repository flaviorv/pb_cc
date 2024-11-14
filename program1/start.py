from show import *
from graph import graph

def initial_menu():
	option = ''
	while option != 'exit':
		shuffle(files)
		print('============== SORTING ALGORITHMS ==============')
		print('Type 1 to print the lists')
		print('Type 2 to show execution time')
		print('Type 3 to generate a graphic')
		print('Type 4 to erase data')
		print('Type 0 to exit')
		option = input()
		match(option):
			case '1':
				prints_menu()
			case '2':
				shuffle_algorithms()
			case '3':
				graph()
			case '4':
				erase_data()
			case '0':
				print('Exiting the application')
				option = 'exit'
			case _:
				print('Invalid command')


def prints_menu():
	option = ""
	while option != 'exit':
		print("======================== LISTS ========================")
		print("Type 1 to print an unordered list")
		print("Type 2 to print a list ordered by Bubble Sort")
		print("Type 3 to print a list ordered by Selection Sort")
		print("Type 4 to print a list ordered by Insertion Sort")
		print("Type 0 to returning to the initial menu")
		option = input()
		match(option):
			case '1':
				print(" - UNORDERED LIST - ")
				show('unordered')
			case '2':
				print(" - BUBBLE SORT LIST - ")
				show('bubble')
			case '3':
				print(" - SELECTION SORT LIST - ")
				show('selection')
			case '4':
				print(" - INSERTION SORT LIST - ")
				show('insertion')
			case '0':
				print('Returning...')
				option = 'exit'
			case _:
				print("Invalid command")



initial_menu()
