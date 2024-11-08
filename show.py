from tp1 import *
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

list = only_name()

print("Bubble Sort")
bubble = bubble_sort(list)
print("Is sorted:", is_sorted(list, bubble))
print()
print("Insertion Sort")
insertion = insertion_sort(list)
print("Is sorted:", is_sorted(list, insertion))
print()
print("Selection Sort")
selection = selection_sort(list)
print("Is sorted", is_sorted(list, selection))

