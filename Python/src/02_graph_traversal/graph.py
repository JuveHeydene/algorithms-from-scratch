"""The graph representation used by every algorithm of the graph traversal family.

A graph is stored as an adjacency list: a dictionary that maps each vertex to
the list of its neighbours. The order of that list matters: the algorithms
always look at the neighbours in the order they are written.

Undirected graph: every edge is written twice (``A -> B`` and ``B -> A``).
Directed graph: an edge is written once, from its start to its end.

A vertex that only appears as a neighbour (never as a key) has no outgoing
edge: use ``graph.get(vertex, [])`` to read its neighbours safely.
"""

from __future__ import annotations

from collections.abc import Hashable

Vertex = Hashable
Graph = dict[Vertex, list[Vertex]]


def sample_graph() -> Graph:
    """Build the undirected graph drawn in every figure of this course.

    ::

                G
               /
              E
             / \\
            A   C
             \\  |
              B-D---F
    """
    return {
        "A": ["B", "E"],
        "B": ["A", "D"],
        "C": ["D", "E"],
        "D": ["B", "C", "F"],
        "E": ["A", "C", "G"],
        "F": ["D"],
        "G": ["E"],
    }


def chain_graph(n: int) -> Graph:
    """Build the directed path ``0 -> 1 -> 2 -> ... -> n - 1``."""
    return {i: [i + 1] if i + 1 < n else [] for i in range(n)}
