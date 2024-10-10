import unittest
from add import addition

class Testcase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addition(10, 20), 30)
        self.assertEqual(addition(100, 20), 120)

if __name__ == '__main__':
    unittest.main()