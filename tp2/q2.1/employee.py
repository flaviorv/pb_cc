from random import uniform, choice, randrange
from decimal import Decimal, ROUND_HALF_DOWN
import copy

class Employee():
    employees = []

    def __init__(self, name: str, salary: float):
        self.name = name
        salary = Decimal(salary)
        salary = salary.quantize(Decimal("0.00"), ROUND_HALF_DOWN)
        self._salary = salary
        self.employees.append(self)

    def get_salary(self):
        return f"${self._salary}"

    salary = property(get_salary)

    @staticmethod
    def get_copy():
        return copy.deepcopy(Employee.employees)

    def __str__(self):
        return f"Salary: {self.salary:<10} Employee: {self.name:<10}"

    @staticmethod    
    def sorting (arr):
        if len(arr) <= 1:
            return arr
        
        stack = [(0, len(arr)-1)]

        while stack:
            start, end = stack.pop()
            if start >= end:
                continue
            pivot_index = Employee.__sorting_pivot(arr, start, end)

            stack.append((start, pivot_index-1))
            stack.append((pivot_index+1, end))

        return arr
    
    @staticmethod
    def __sorting_pivot(arr, start, end):
        pivot_index = randrange(start, end+1)
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        pivot_index = end
        pivot = arr[pivot_index]
        
        i = start-1

        for j in range(start, end):
            if arr[j]._salary <= pivot._salary:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]
        
        new_pivot_index = i+1
        arr[new_pivot_index], arr[pivot_index] = arr[pivot_index], arr[new_pivot_index]
        return new_pivot_index


names = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana", "Kevin", "Larissa"]

e1 = Employee(choice(names), uniform(500, 10000))
e2 = Employee(choice(names), uniform(500, 10000))
e3 = Employee(choice(names), uniform(500, 10000))
e4 = Employee(choice(names), uniform(500, 10000))
e5 = Employee(choice(names), uniform(500, 10000))
e6 = Employee(choice(names), uniform(500, 10000))
e7 = Employee(choice(names), uniform(500, 10000))
e8 = Employee(choice(names), uniform(500, 10000))
e9 = Employee(choice(names), uniform(500, 10000))
e10 = Employee(choice(names), uniform(500, 10000))
e11 = Employee(choice(names), uniform(500, 10000))
e12 = Employee(choice(names), uniform(500, 10000))

unordered = Employee.get_copy()
Employee.sorting(Employee.employees)
ordered = Employee.get_copy()

print(f"{"Unordered":>24} {"Sorted":>50}")
for u, o in zip(unordered, ordered):
    print(f"\033[31m \033[1m {u.__str__():<50}\033[0m  \033[32m \033[1m{o.__str__():<50}")


