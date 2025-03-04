import unittest
from fibonacci import fib, memofib

class Test(unittest.TestCase):
    def test_fib(self):
        print("\33[33mWithout Memorization\33[0m")
        results = []
        for i in range(11):
            print(f"Position {i}")
            result, iterations = fib(i)
            print(f"\33[32mResult = {result}, \33[31mIterations = {iterations}\33[0m")
            if len(results) >= 2:
                self.assertEqual(results[i-1] + results[i-2], result)
            results.append(result)

    def test_memofib(self):
        print("\33[33mWith Memorization\33[0m")
        results = []
        for i in range(11):
            print(f"Position {i}")
            result, iterations = memofib(i, {})
            print(f"\33[32mResult = {result}, \33[31mIterations = {iterations}\33[0m")
            if len(results) >= 2:
                self.assertEqual(results[i-1] + results[i-2], result)
            results.append(result)

    #The recursive Fibonacci without memorization has an exponential time complexity.
    #For each number, all previous numbers are recalculated
    #Iterations n-1 ~ (1.6^n)
    #Big O = O(2^n)

    #With memorization, the time complexity is equals to O(n), because there is no recalculation.
    #The values are kept in an dict to be returned when needed.

if __name__ == "__main__":
    print("Factorial methods comparison:")
    unittest.main()