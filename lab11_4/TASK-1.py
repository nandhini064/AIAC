from __future__ import annotations
from typing import Generic, List, TypeVar
T = TypeVar("T")
class Stack(Generic[T]):
    """A simple LIFO stack implementation.

    Supports push, pop, peek, is_empty operations and len().
    """

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Push an item on top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item.

        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Return the top item without removing it.

        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no items."""
        return len(self._items) == 0

    def __len__(self) -> int:  # Allows using len(stack)
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack(top->bottom): {list(reversed(self._items))}"


def _demo() -> None:
    stack: Stack[int] = Stack()
    print("Initial:", stack, "empty=", stack.is_empty())

    for value in (10, 20, 30):
        print("push", value)
        stack.push(value)
        print("  ", stack)

    print("peek ->", stack.peek())
    print("after peek:", stack)

    while not stack.is_empty():
        print("pop ->", stack.pop())
        print("  ", stack)

    print("empty=", stack.is_empty())


if __name__ == "__main__":
    _demo()
