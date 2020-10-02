import unittest
from store import coupon_calculations as coupon

class test(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(8.80, coupon.calculate_price(7.99, 5, 10), 2)
        self.assertAlmostEqual(5.039, coupon.calculate_price(3.99, 5, 15), 2)
        self.assertAlmostEqual(9.33, coupon.calculate_price(8.99, 5, 20), 2)
        self.assertAlmostEqual(1.17, coupon.calculate_price(4.99, 10, 10), 2)
        self.assertAlmostEqual(5.94, coupon.calculate_price(9.99, 10, 20), 2)
        self.assertAlmostEqual(4.03, coupon.calculate_price(2.99, 5, 10), 2)
    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(30.84, coupon.calculate_price(28.99, 5, 10), 2)
        self.assertAlmostEqual(13.15, coupon.calculate_price(12.99, 5, 15), 2)
        self.assertAlmostEqual(15.27, coupon.calculate_price(15.99, 5, 20), 2)
        self.assertAlmostEqual(6.89, coupon.calculate_price(10.99, 10, 10), 2)
        self.assertAlmostEqual(10.18, coupon.calculate_price(14.99, 10, 20), 2)
        self.assertAlmostEqual(18.965, coupon.calculate_price(17.99, 5, 20), 2)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(37.514, coupon.calculate_price(35.99, 5, 10), 2)
        self.assertAlmostEqual(33.17, coupon.calculate_price(32.99, 5, 15), 2)
        self.assertAlmostEqual(36.77, coupon.calculate_price(38.99, 5, 20), 2)
        self.assertAlmostEqual(33.70, coupon.calculate_price(36.99, 10, 10), 2)
        self.assertAlmostEqual(38.47, coupon.calculate_price(40.99, 5, 20), 2)
        self.assertAlmostEqual(38.47, coupon.calculate_price(45.99, 10, 20), 2)
    def test_price_under_over_fifty(self):
        self.assertAlmostEqual(62.50, coupon.calculate_price(57.99, 5, 10), 2)
        self.assertAlmostEqual(72.97, coupon.calculate_price(85.99, 5, 15), 2)
        self.assertAlmostEqual(89.88, coupon.calculate_price(110.99, 5, 20), 2)
        self.assertAlmostEqual(62.95, coupon.calculate_price(75.99, 10, 10), 2)
        self.assertAlmostEqual(140.76, coupon.calculate_price(170.99, 5, 20), 2)
        self.assertAlmostEqual(161.96, coupon.calculate_price(200.99, 10, 20), 2)

if __name__ == '__main__':
    unittest.main()
