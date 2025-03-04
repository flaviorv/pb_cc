from save_times import save_times
import unittest
import hanoi_tower
import chart

class Test(unittest.TestCase):

    def test_input_greater_than_0(self):
        print("Input size test")
        self.assertEqual(hanoi_tower.init(-1), "Discs must be greater than 0")
        self.assertEqual(hanoi_tower.init(0), "Discs must be greater than 0")
    
    def test_input_is_int(self):
        print("Input type test")
        self.assertEqual(hanoi_tower.init(1.5), "Discs must be an integer")
        self.assertEqual(hanoi_tower.init(0.5), "Discs must be an integer")

if __name__ == "__main__":
    save_times(22)
    chart.generate_chart()
    unittest.main()
    
        
