from automated import *

def init_menu():
	option = ''
	while option != 'exit_app':
		print('=========== CHOOSE A DATA STRUCTURE ===========')
		print('----------------------------------------------')
		print('Type 1 to Hash Table')
		print('Type 2 to Queue')
		print('Type 3 to Stack')
		print('Type 4 to print the data that will be used')
		print('Type 0 to exit')
		print('----------------------------------------------')
		option = input()
		match(option):
			case '1':
				hash_menu()
			case '2':
				queue_menu()
			case '3':
				stack_menu()
			case '4':
				show_files()
			case '0':
				print('Exiting the application')
				option = 'exit_app'
			case _:
				print('Invalid command')


def hash_menu():
	option = ''
	while option != 'exit_hash':
		print('================== HASH TABLE ==================')
		print('----------------------------------------------')
		print('Type 1 to fill table')
		print('Type 2 to perform the automated search')
		print('Type 3 to add an element in the table')
		print('Type 4 to search for an element')
		print('Type 5 to remove an element from the table')
		print('Type 6 to show all keys')
		print('Type 7 to show the table')
		print('Type 0 to return to the initial menu')
		print('----------------------------------------------')
		option = input()
		match(option):
			case '1':
				fill_table()
			case '2':
				hash_search()
			case '3':
				key = input('Type the element key: ')
				value = input('Type the element value: ')
				add_hash(key, value)
			case '4':
				key = input('Type the element key: ')
				print(get_element(key))
			case '5':
				key = input('Type the key to remove the element: ')
				rm_hash(key)
			case '6':
				all_keys()
			case '7':
				show_table()
			case '0':
				print('Returning...')
				option = 'exit_hash'
			case _:
				print('Invalid command')



def queue_menu():
	option = ''
	while option != 'exit_queue':
		print('==================== QUEUE ====================')
		print('----------------------------------------------')
		print('Type 1 to fill the queue')
		print('Type 2 to perform the automated search')
		print('Type 3 to enqueue an element')
		print('Type 4 to dequeue an element')
		print('Type 5 to show the queue')
		print('Type 0 to return to the initial menu')
		print('----------------------------------------------')
		option = input()
		match(option):
			case '1':
				fill_queue()
			case '2':
				queue_search()
			case '3':
				element = input('Type the element: ')
				add_queue(element)
			case '4':
				rm_queue()
			case '5':
				show_queue()
			case '0':
				print('Returning...')
				option = 'exit_queue'




def stack_menu():
	option = ''
	while option != 'exit_stack':
		print('==================== STACK ====================')
		print('----------------------------------------------')
		print('Type 1 to fill the stack')
		print('Type 2 to perform the automated search')
		print('Type 3 to stack an element')
		print('Type 4 to unstack an element')
		print('Type 5 to show the stack')
		print('Type 0 to return to the initial menu')
		print('----------------------------------------------')
		option = input()
		match(option):
			case '1':
				fill_stack()
			case '2':
				stack_search()
			case '3':
				element = input('Type the element: ')
				add_stack(element)
			case '4':
				rm_stack()
			case '5':
				show_stack()
			case '0':
				print('Returning...')
				option = 'exit_stack'



init_menu()
