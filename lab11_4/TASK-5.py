from __future__ import annotations
from collections import deque
from typing import Deque, Dict, Generic, Iterable, List, Set, TypeVar
T = TypeVar("T")
class Graph(Generic[T]):
    """Adjacency-list graph with BFS and DFS traversals.

    By default the graph is undirected. Set directed=True for a directed graph.
    """

    def __init__(self, directed: bool = False) -> None:
        self._adj: Dict[T, List[T]] = {}
        self._directed: bool = directed

    def add_vertex(self, v: T) -> None:
        if v not in self._adj:
            self._adj[v] = []

    def add_edge(self, u: T, v: T) -> None:
        """Add edge u->v. Adds missing vertices automatically.

        For undirected graphs, also adds v->u.
        """
        if u not in self._adj:
            self._adj[u] = []
        if v not in self._adj:
            self._adj[v] = []

        self._adj[u].append(v)
        if not self._directed:
            self._adj[v].append(u)

    def neighbors(self, v: T) -> List[T]:
        return self._adj.get(v, [])

    def bfs(self, start: T) -> List[T]:
        """Breadth-first traversal starting at start; returns visited order."""
        if start not in self._adj:
            return []

        visited: Set[T] = set([start])
        order: List[T] = []
        queue: Deque[T] = deque([start])

        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in self._adj[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        return order

    def dfs(self, start: T) -> List[T]:
        """Depth-first traversal (iterative) starting at start; returns order."""
        if start not in self._adj:
            return []

        visited: Set[T] = set()
        order: List[T] = []
        stack: List[T] = [start]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            # Push neighbors in reverse to visit in original insertion order
            neighbors = self._adj[node]
            for nxt in reversed(neighbors):
                if nxt not in visited:
                    stack.append(nxt)
        return order

    # Uppercase aliases, if you prefer BFS()/DFS() naming
    def BFS(self, start: T) -> List[T]:
        return self.bfs(start)

    def DFS(self, start: T) -> List[T]:
        return self.dfs(start)

    def __repr__(self) -> str:
        return f"Graph(directed={self._directed}, adj={self._adj})"


def _demo() -> None:
    # Undirected example
    g = Graph[int]()
    edges: Iterable[tuple[int, int]] = [
        (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 6)
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print("Adjacency:", g)
    print("BFS from 1:", g.BFS(1))
    print("DFS from 1:", g.DFS(1))

    # Directed example
    dg = Graph[int](directed=True)
    for u, v in [(1, 2), (2, 3), (1, 3), (3, 4)]:
        dg.add_edge(u, v)
    print("\nDirected graph adjacency:", dg)
    print("BFS from 1:", dg.BFS(1))
    print("DFS from 1:", dg.DFS(1))


if __name__ == "__main__":
    _demo()
