import unittest
import main


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(10, 5), 15)
        

    def test_subtract(self):
        self.assertEqual(main.subtract(10, 5), 5)
        

    def test_multiply(self):
        self.assertEqual(main.multiply(10, 5), 50)
        

    def test_divide(self):
        self.assertEqual(main.divide(10, 5), 2)
        self.assertEqual(main.divide(-1, 1), -1)
        

        with self.assertRaises(ValueError):
            main.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
