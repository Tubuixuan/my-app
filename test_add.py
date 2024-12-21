# test_add.py
import unittest
from add import add  # Import hàm add đã tạo

class TestAddFunction(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
