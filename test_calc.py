import unittest
import calc


class MyTestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(20, 30), 50)
        self.assertNotEqual(calc.add(20, 30), 0)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(20, 30), -10)
        self.assertNotEqual(calc.sub(20, 30), 0)

    def test_mul(self):
        self.assertEqual(calc.mul(10, 5), 50)
        self.assertEqual(calc.mul(20, 30), 600)
        self.assertNotEqual(calc.mul(20, 30), 0)

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(20, 30), 2/3)
        self.assertNotEqual(calc.div(20, 30), 0)


if __name__ == '__main__':
    unittest.main()
