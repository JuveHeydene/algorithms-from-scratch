"""Level-order traversal (breadth-first on a tree): level by level, left to right.

The course is in the README.md of this folder. Replace every
``raise NotImplementedError`` with my own implementation, then run:

    pytest -k level_order
"""

from __future__ import annotations

from binary_tree import Node


def level_order(root: Node | None) -> list:
    """Return the values of the tree level by level, from left to right.

    Use a queue (``collections.deque``).
    Example with ``sample_tree()``: ``['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H']``.
    An empty tree (``None``) gives ``[]``.
    """
    raise NotImplementedError("TODO: level_order")


def levels(root: Node | None) -> list[list]:
    """Return one list per level.

    Example with ``sample_tree()``:
    ``[['F'], ['B', 'G'], ['A', 'D', 'I'], ['C', 'E', 'H']]``.
    """
    raise NotImplementedError("TODO: levels")


def right_side_view(root: Node | None) -> list:
    """Return what I would see standing on the right of the tree: the last node of each level.

    Example with ``sample_tree()``: ``['F', 'G', 'I', 'H']``.
    """
    raise NotImplementedError("TODO: right_side_view")
