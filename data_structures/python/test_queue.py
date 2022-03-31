import unittest

from queue import Queue, QueueEmptyException
 

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.assertTrue(self.queue.is_empty)

        self.queue.enqueue(1)
        self.assertEqual(self.queue.size, 1)
        self.assertFalse(self.queue.is_empty)

        self.queue.enqueue(2)
        self.assertEqual(self.queue.size, 2)
        self.assertFalse(self.queue.is_empty)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size, 1)
        self.assertFalse(self.queue.is_empty)

        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.size, 0)
        self.assertTrue(self.queue.is_empty)

        self.assertRaises(QueueEmptyException, self.queue.dequeue)

    def tearDown(self):
        self.queue.clear()


if __name__ == "__main__":
    unittest.main()
