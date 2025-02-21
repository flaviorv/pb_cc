import unittest
from factorial import factorial

class Test(unittest.TestCase):
    def test_factorial(self):
        factorials = []
        for i in range(10):
            f, it = factorial(i)
            if len(factorials) > 0:
                self.assertEqual(f, i*factorials[i-1])
            else:
                self.assertEqual(f, 1)
            factorials.append(f)
            print(f"{i} factorial = {f}, Iterations = {it}")

       
# The time complexiy is O(n), because the number of iterations is the input number
if __name__ == "__main__":
    unittest.main()