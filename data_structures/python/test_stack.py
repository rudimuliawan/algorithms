import unittest

from stack import Stack, StackEmptyException
 

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
    
    def test_push(self):
        self.assertTrue(self.stack.is_empty)

        self.stack.push(1)
        self.assertEqual(self.stack.top, 1)
        self.assertEqual(self.stack.size, 1)
        self.assertFalse(self.stack.is_empty)

        self.stack.push(2)
        self.assertEqual(self.stack.top, 2)
        self.assertEqual(self.stack.size, 2)
        self.assertFalse(self.stack.is_empty)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size, 1)
        self.assertFalse(self.stack.is_empty)

        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.size, 0)
        self.assertTrue(self.stack.is_empty)

        self.assertRaises(StackEmptyException, self.stack.pop)

    def tearDown(self):
        self.stack.clear()


if __name__ == "__main__":
    unittest.main()
