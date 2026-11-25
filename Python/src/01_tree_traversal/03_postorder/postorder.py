"""Postorder traversal: left subtree -> right subtree -> node.

The course is in the README.md of this folder. Replace every
``raise NotImplementedError`` with my own implementation, then run:

    pytest -k postorder
"""

from __future__ import annotations

from binary_tree import Node


def postorder(root: Node | None) -> list:
    """Return the values of the tree in postorder, using recursion.

    Example with ``sample_tree()``: ``['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']``.
    An empty tree (``None``) gives ``[]``.
    """
    raise NotImplementedError("TODO: postorder (recursive)")


def postorder_iterative(root: Node | None) -> list:
    """Same result as ``postorder``, without recursion.

    Use one or two explicit stacks. It must work on a tree 10,000 levels deep.
    """
    raise NotImplementedError("TODO: postorder (iterative)")


def evaluate(root: Node) -> float:
    """Compute the value of an expression tree.

    Operators: ``"+"``, ``"-"``, ``"*"``, ``"/"`` (true division).
    Example with ``expression_tree()``: ``21``.
    """
    raise NotImplementedError("TODO: evaluate")


def height(root: Node | None) -> int:
    """Return the number of levels of the tree.

    Empty tree: ``0``. A single node: ``1``. ``sample_tree()``: ``4``.
    """
    raise NotImplementedError("TODO: height")
