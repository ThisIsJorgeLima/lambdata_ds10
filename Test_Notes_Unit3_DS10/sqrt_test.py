import unittest
from sqrt import lazy_sqrt, builtin_sqrt, newton_sqrt1

class SqrtTests(unittest.TestCase):
    """obligatory docstring, tests square root functions"""
    def test_sqrt9(self):
        self.assertEqual(newton_sqrt1(9), 3)

if __name__ == '__main__':
    unittest.main()
