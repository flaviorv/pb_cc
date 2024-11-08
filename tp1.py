def only_name():
	file = open('files.txt', 'r')
	files = file.readlines()

	for i in range(len(files)):
		files[i] = files[i].replace('.txt\n', '')

	return files

def is_sorted(list, sorted):
	list.sort()
	if len(list) != len(sorted):
		return False
	for i in range(len(list)):
		if list[i] != sorted[i]:
			return False
	return True
