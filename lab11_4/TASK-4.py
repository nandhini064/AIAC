from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, List, Optional, TypeVar


T = TypeVar("T")


@dataclass
class _BSTNode(Generic[T]):
    key: T
    left: Optional["_BSTNode[T]"] = None
    right: Optional["_BSTNode[T]"] = None


class BinarySearchTree(Generic[T]):
    """A simple unbalanced Binary Search Tree (BST).

    Assumes keys are comparable with < and >.
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._root: Optional[_BSTNode[T]] = None
        self._size: int = 0
        if values is not None:
            for v in values:
                self.insert(v)

    def insert(self, key: T) -> None:
        """Insert key into the BST. Duplicates go to the right subtree."""
        if self._root is None:
            self._root = _BSTNode(key)
            self._size = 1
            return

        current = self._root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = _BSTNode(key)
                    self._size += 1
                    return
                current = current.left
            else:  # key >= current.key -> go right (place duplicates on right)
                if current.right is None:
                    current.right = _BSTNode(key)
                    self._size += 1
                    return
                current = current.right

    def search(self, key: T) -> bool:
        """Return True if key exists in the BST, else False."""
        current = self._root
        while current is not None:
            if key == current.key:
                return True
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self) -> List[T]:
        """Return the keys in ascending order using in-order traversal."""
        result: List[T] = []

        def _inorder(node: Optional[_BSTNode[T]]) -> None:
            if node is None:
                return
            _inorder(node.left)
            result.append(node.key)
            _inorder(node.right)

        _inorder(self._root)
        return result

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"BST[n={self._size}] {self.inorder_traversal()}"


def _demo() -> None:
    bst = BinarySearchTree[int]([7, 3, 9, 1, 5, 8, 10, 5])
    print("Initial:", bst)

    for k in (0, 1, 5, 6, 10, 11):
        print(f"search({k}) ->", bst.search(k))

    print("Insert 6, 2, 12")
    for k in (6, 2, 12):
        bst.insert(k)
        print("  ", bst)

    print("inorder_traversal ->", bst.inorder_traversal())


if __name__ == "__main__":
    _demo()
