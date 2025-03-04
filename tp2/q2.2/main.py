from random import uniform, randrange
from decimal import Decimal, ROUND_HALF_DOWN
from fake_names import create_names
import copy


class Employee():
    employees = []

    names = create_names(20)

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
    def fill():
        names = copy.deepcopy(Employee.names)
        for _ in range(len(names)):
            Employee(names.pop(), uniform(500, 10000))

    @staticmethod    
    def sorting (pivot_type):
        arr = Employee.employees
        if len(arr) <= 1:
            return arr
        
        stack = [(0, len(arr)-1)]

        while stack:
            start, end = stack.pop()
            if start >= end:
                continue
            
            pivot_index = Employee.__choosing_pivot(start, end, pivot_type)
            pivot_index = Employee.__sorting_pivot(arr, start, end, pivot_index)

            stack.append((start, pivot_index-1))
            stack.append((pivot_index+1, end))

        return arr
    
    @staticmethod
    def __choosing_pivot(start, end, pivot_type):
        match(pivot_type):
            case "start":
                return start
            case "middle":
                index = (start + end) // 2
                return index
            case "end":
                return end
            case "random":
                return randrange(start, end+1)


    @staticmethod
    def __sorting_pivot(arr, start, end, pivot_index):
        if pivot_index != end:
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

def main():
        Employee.fill()
        unordered = Employee.get_copy()
        Employee.sorting("random")
        ordered = Employee.employees
        
        print(f"\033[34m \033[1m{"Unordered":>26} {"Sorted":>57}")
        print("\033[1m \033[34m---------------------------------------------------------------------------------------------------------------------------")
        for u, o in zip(unordered, ordered):
            print(f"\033[34m | \033[31m \033[1m {u.__str__():<55} \033[34m | \033[32m \033[1m{o.__str__():<55} \033[1m \033[34m |")
        print("\033[1m \033[34m---------------------------------------------------------------------------------------------------------------------------")

        Employee.employees = []


if __name__ == "__main__":
    main()