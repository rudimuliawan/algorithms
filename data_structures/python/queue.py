class QueueEmptyException(Exception):

    def __init__(self, message):
        self.message = message


class Queue:
    
    class Node:
        
        def __init__(self, item) -> None:
            self.item = item
            self.next = None

    def __init__(self) -> None:
        self._first = None
        self._last = None
        self._size = 0

    def enqueue(self, item):
        old_last = self._last
        self._last = self.Node(item)
        
        if self.is_empty:
            self._first = self._last
        else:
            old_last.next = self._last

        self._size += 1

    def dequeue(self):
        if self.is_empty:
            raise QueueEmptyException("dequeue() aborted, queue is empty")
        
        item = self._first.item
        self._first = self._first.next
        self._size -= 1

        if (self.is_empty):
            self._last = None

        return item

    def clear(self):
        while not self.is_empty:
            _ = self.dequeue()

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0
