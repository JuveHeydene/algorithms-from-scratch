"""Inorder traversal: left subtree -> node -> right subtree.

The course is in the README.md of this folder. Replace every
``raise NotImplementedError`` with my own implementation, then run:

    pytest -k inorder
"""

from __future__ import annotations

from binary_tree import Node


def inorder(root: Node | None) -> list:
    """Return the values of the tree in inorder, using recursion.

    Example with ``sample_tree()``: ``['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']``.
    An empty tree (``None``) gives ``[]``.
    """
    raise NotImplementedError("TODO: inorder (recursive)")


def inorder_iterative(root: Node | None) -> list:
    """Same result as ``inorder``, without recursion.

    Use an explicit stack. It must work on a tree 10,000 levels deep.
    """
    raise NotImplementedError("TODO: inorder (iterative, with a stack)")


def to_infix(root: Node | None) -> str:
    """Write an expression tree in infix notation, with every operation in parentheses.

    Example with ``expression_tree()``: ``'((3 + 4) * (5 - 2))'``.
    A single leaf is written without parentheses: ``Node(7)`` gives ``'7'``.
    An empty tree gives ``''``.
    """
    raise NotImplementedError("TODO: to_infix")


def is_binary_search_tree(root: Node | None) -> bool:
    """Tell whether the tree is a binary search tree.

    A binary search tree is a tree whose inorder traversal is strictly
    increasing. ``sample_tree()`` is one; an empty tree is one too.
    """
    raise NotImplementedError("TODO: is_binary_search_tree")
