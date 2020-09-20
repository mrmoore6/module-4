import unittest
from input_validation import validation_with_try

class MyTestCase(unittest.TestCase):
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 80, 79)
        with self.assertRaises(ValueError):
            validation_with_try.average(90, -60, 40)
        with self.assertRaises(ValueError):
                validation_with_try.average(90, 60, -30)
if __name__ == '__main__':
    unittest.main()
#test
