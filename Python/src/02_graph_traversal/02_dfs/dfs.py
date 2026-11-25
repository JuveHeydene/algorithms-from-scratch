"""Depth-First Search (DFS): go as deep as possible, then backtrack.

The course is in the README.md of this folder. Replace every
``raise NotImplementedError`` with my own implementation, then run:

    pytest -k dfs
"""

from __future__ import annotations

from graph import Graph, Vertex


def dfs(graph: Graph, start: Vertex) -> list[Vertex]:
    """Return the vertices reachable from ``start``, in the order DFS discovers them, using recursion.

    Neighbours are explored in the order of their adjacency list.
    Example with ``sample_graph()`` from ``"A"``: ``['A', 'B', 'D', 'C', 'E', 'G', 'F']``.
    """
    raise NotImplementedError("TODO: dfs (recursive)")


def dfs_iterative(graph: Graph, start: Vertex) -> list[Vertex]:
    """Same result as ``dfs``, in the same order, without recursion: use an explicit stack.

    It must work on a path of 10,000 vertices, where recursion would crash.
    """
    raise NotImplementedError("TODO: dfs (iterative, with a stack)")


def find_path(graph: Graph, start: Vertex, goal: Vertex) -> list[Vertex] | None:
    """Return the first path from ``start`` to ``goal`` that DFS finds, both included.

    It is a valid path, not necessarily the shortest one.
    Return ``[start]`` when ``start == goal`` and ``None`` when ``goal`` cannot be reached.
    Example with ``sample_graph()``: ``find_path(g, "A", "F") == ['A', 'B', 'D', 'F']``.
    """
    raise NotImplementedError("TODO: find_path")
