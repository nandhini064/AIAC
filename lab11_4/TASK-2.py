from __future__ import annotations
from typing import Deque, Generic, TypeVar
from collections import deque
T = TypeVar("T")
class Queue(Generic[T]):
    """A simple FIFO queue implementation.

    Supports enqueue, dequeue, is_empty operations and len().
    """

    def __init__(self) -> None:
        self._items: Deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self) -> T:
        """Remove and return the item from the front of the queue.

        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self) -> bool:
        """Return True if the queue has no items."""
        return len(self._items) == 0
    def __len__(self) -> int:  # Allows using len(queue)
        return len(self._items)
    def __repr__(self) -> str:
        return f"Queue(front->back): {list(self._items)}"
def _demo() -> None:
    queue: Queue[int] = Queue()
    print("Initial:", queue, "empty=", queue.is_empty())

    for value in (1, 2, 3):
        print("enqueue", value)
        queue.enqueue(value)
        print("  ", queue)
    while not queue.is_empty():
        print("dequeue ->", queue.dequeue())
        print("  ", queue)
    print("empty=", queue.is_empty())
if __name__ == "__main__":
    _demo()
