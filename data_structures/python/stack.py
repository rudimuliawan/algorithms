class StackEmptyException(Exception):

    def __init__(self, message):
        self.message = message


class Stack:

    class Node:

        def __init__(self, item) -> None:
            self.item = item
            self.next = None

    def __init__(self) -> None:
        self._size = 0
        self._top = None

    def push(self, item):
        old_top = self._top
        self._top = self.Node(item)
        self._top.next = old_top
        self._size += 1

    def pop(self):
        if self.is_empty:
            raise StackEmptyException(
                "pop() aborted, stack is empty"
            )

        item = self._top.item
        self._top = self._top.next
        self._size -= 1
        return item

    def clear(self):
        while self.top is not None:
            _ = self.pop()

    @property
    def top(self):
        if self._top is not None:
            return self._top.item

        return None

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self.size == 0
