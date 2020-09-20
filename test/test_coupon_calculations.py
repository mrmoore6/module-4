import unittest
from store import coupon_calculations as coupon

class test(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(8.80, coupon.calculate_price(7.99, 5, 10), 2)
        self.assertAlmostEqual(5.039, coupon.calculate_price(3.99, 5, 15), 2)
        self.assertAlmostEqual(9.33, coupon.calculate_price(8.99, 5, 20), 2)
        self.assertAlmostEqual(1.17, coupon.calculate_price(4.99, 10, 10), 2)
    def test_price_under_thirty(self):
        self.assertAlmostEqual(23.99, coupon.calculate_price(28.99, 5, 10), 2)
        self.assertAlmostEqual(18.99, coupon.calculate_price(12.99, 5, 15), 2)
        self.assertAlmostEqual(19.99, coupon.calculate_price(15.99, 5, 20), 2)
        self.assertAlmostEqual(27.99, coupon.calculate_price(10.99, 10, 10), 2)
if __name__ == '__main__':
    unittest.main()
