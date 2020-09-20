import unittest
from store import coupon_calculations as coupon

class test(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(8.80, coupon.calculate_price(7.99, 5, 10), 2)
        self.assertAlmostEqual(5.039, coupon.calculate_price(3.99, 5, 15), 2)
        self.assertAlmostEqual(9.33, coupon.calculate_price(8.99, 5, 20), 2)
        self.assertAlmostEqual(1.17, coupon.calculate_price(4.99, 10, 10), 2)
    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(30.84, coupon.calculate_price(28.99, 5, 10), 2)
        self.assertAlmostEqual(13.15, coupon.calculate_price(12.99, 5, 15), 2)
        self.assertAlmostEqual(15.27, coupon.calculate_price(15.99, 5, 20), 2)
        self.assertAlmostEqual(6.89, coupon.calculate_price(10.99, 10, 10), 2)
    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(37.514, coupon.calculate_price(35.99, 5, 10), 2)
        self.assertAlmostEqual(33.17, coupon.calculate_price(32.99, 5, 15), 2)
        self.assertAlmostEqual(36.77, coupon.calculate_price(38.99, 5, 20), 2)
        self.assertAlmostEqual(33.70, coupon.calculate_price(36.99, 10, 10), 2)
if __name__ == '__main__':
    unittest.main()
