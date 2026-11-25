"""Preorder traversal: node -> left subtree -> right subtree.

The course is in the README.md of this folder. Replace every
``raise NotImplementedError`` with my own implementation, then run:

    pytest -k preorder
"""

from __future__ import annotations

from binary_tree import Node


def preorder(root: Node | None) -> list:
    """Return the values of the tree in preorder, using recursion.

    Example with ``sample_tree()``: ``['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']``.
    An empty tree (``None``) gives ``[]``.
    """
    raise NotImplementedError("TODO: preorder (recursive)")


def preorder_iterative(root: Node | None) -> list:
    """Same result as ``preorder``, without recursion.

    Use an explicit stack (a Python list with ``append`` / ``pop``).
    It must work on a tree 10,000 levels deep, where recursion would crash.
    """
    raise NotImplementedError("TODO: preorder (iterative, with a stack)")


def to_prefix(root: Node | None) -> str:
    """Write an expression tree in prefix notation, tokens separated by one space.

    Example with ``expression_tree()``: ``'* + 3 4 - 5 2'``.
    An empty tree gives ``''``.
    """
    raise NotImplementedError("TODO: to_prefix")
