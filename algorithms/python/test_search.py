import unittest

from search import binary_search


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.data1 = [10, 20, 30, 40, 50, 60]
        self.data2 = [10, 20, 30, 40, 50, 60, 70]

    def test_search_even(self):
        self.assertEqual(binary_search(self.data1, 30), 2)
        self.assertIsNone(binary_search(self.data1, 70))

    def test_search_odd(self):
        self.assertEqual(binary_search(self.data2, 50), 4)
        self.assertIsNone(binary_search(self.data2, 80))


if __name__ == "__main__":
    unittest.main()
