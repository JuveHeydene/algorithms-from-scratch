"""Breadth-First Search (BFS): explore a graph in waves, closest vertices first.

The course is in the README.md of this folder. Replace every
``raise NotImplementedError`` with my own implementation, then run:

    pytest -k bfs
"""

from __future__ import annotations

from graph import Graph, Vertex


def bfs(graph: Graph, start: Vertex) -> list[Vertex]:
    """Return the vertices reachable from ``start``, in the order BFS discovers them.

    Neighbours are explored in the order of their adjacency list.
    Example with ``sample_graph()`` from ``"A"``: ``['A', 'B', 'E', 'D', 'C', 'G', 'F']``.
    """
    raise NotImplementedError("TODO: bfs")


def bfs_distances(graph: Graph, start: Vertex) -> dict[Vertex, int]:
    """Return the number of edges of the shortest path from ``start`` to every reachable vertex.

    Example with ``sample_graph()`` from ``"A"``:
    ``{'A': 0, 'B': 1, 'E': 1, 'D': 2, 'C': 2, 'G': 2, 'F': 3}``.
    Unreachable vertices are not in the result.
    """
    raise NotImplementedError("TODO: bfs_distances")


def shortest_path(graph: Graph, start: Vertex, goal: Vertex) -> list[Vertex] | None:
    """Return a path with the fewest edges from ``start`` to ``goal``, both included.

    Return ``[start]`` when ``start == goal`` and ``None`` when ``goal`` cannot be reached.
    Example with ``sample_graph()``: ``shortest_path(g, "A", "F") == ['A', 'B', 'D', 'F']``.
    """
    raise NotImplementedError("TODO: shortest_path")
