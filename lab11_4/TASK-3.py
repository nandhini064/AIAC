from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterator, List, Optional, TypeVar
T = TypeVar("T")
@dataclass
class _Node(Generic[T]):
    value: T
    next: Optional["_Node[T]"] = None
class SinglyLinkedList(Generic[T]):
    """A simple singly linked list with tail pointer for O(1) append."""

    def __init__(self) -> None:
        self._head: Optional[_Node[T]] = None
        self._tail: Optional[_Node[T]] = None
        self._length: int = 0

    def insert_at_end(self, value: T) -> None:
        """Insert a new node containing value at the end of the list."""
        new_node = _Node(value)
        if self._tail is None:
            # Empty list
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._length += 1

    def delete_value(self, value: T) -> bool:
        """Delete the first node whose value equals value.

        Returns True if a node was deleted, otherwise False.
        """
        prev: Optional[_Node[T]] = None
        current = self._head

        while current is not None:
            if current.value == value:
                # Remove current
                if prev is None:
                    # Removing head
                    self._head = current.next
                else:
                    prev.next = current.next

                if current is self._tail:
                    # Removed tail; update tail to prev
                    self._tail = prev

                self._length -= 1
                return True

            prev = current
            current = current.next

        return False

    def traverse(self) -> List[T]:
        """Return a list of values from head to tail."""
        values: List[T] = []
        current = self._head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        return f"SinglyLinkedList[{self._length}]: {self.traverse()}"


def _demo() -> None:
    ll: SinglyLinkedList[int] = SinglyLinkedList()
    print("Initial:", ll)

    for v in (5, 10, 15, 10):
        print("insert_at_end", v)
        ll.insert_at_end(v)
        print("  ", ll)

    print("traverse ->", ll.traverse())

    print("delete_value(10)")
    deleted = ll.delete_value(10)
    print("  deleted=", deleted, "=>", ll)

    print("delete_value(999)")
    deleted = ll.delete_value(999)
    print("  deleted=", deleted, "=>", ll)

    print("delete_value(15)")
    deleted = ll.delete_value(15)
    print("  deleted=", deleted, "=>", ll)

    print("delete_value(5)")
    deleted = ll.delete_value(5)
    print("  deleted=", deleted, "=>", ll)

    print("delete_value(10)")
    deleted = ll.delete_value(10)
    print("  deleted=", deleted, "=>", ll)


if __name__ == "__main__":
    _demo()
