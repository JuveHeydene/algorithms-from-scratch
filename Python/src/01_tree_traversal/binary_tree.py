"""The binary tree used by every algorithm of the tree traversal family.

A tree is never stored "as a whole": we only keep a reference to its root
``Node``. Each node knows its value and its two children (or ``None`` when a
child is missing). An empty tree is simply ``None``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    left: Node | None = None
    right: Node | None = None


def sample_tree() -> Node:
    """Build the tree drawn in every figure of this course.

    ::

                F
              /   \\
             B     G
            / \\     \\
           A   D     I
              / \\   /
             C   E H
    """
    return Node(
        "F",
        left=Node(
            "B",
            left=Node("A"),
            right=Node("D", left=Node("C"), right=Node("E")),
        ),
        right=Node(
            "G",
            right=Node("I", left=Node("H")),
        ),
    )


def expression_tree() -> Node:
    """Build the expression tree of ``(3 + 4) * (5 - 2)``.

    ::

                *
              /   \\
             +     -
            / \\   / \\
           3   4 5   2

    Inner nodes hold an operator as a string (``"+"``, ``"-"``, ``"*"``,
    ``"/"``). Leaves hold a number.
    """
    return Node(
        "*",
        left=Node("+", left=Node(3), right=Node(4)),
        right=Node("-", left=Node(5), right=Node(2)),
    )


def left_chain(n: int) -> Node | None:
    """Build a degenerate tree of ``n`` nodes where every node only has a left child.

    The values are ``0`` (the root) down to ``n - 1`` (the deepest leaf).
    It is built from the bottom up, without recursion, so it works for any ``n``.
    """
    root = None
    for value in reversed(range(n)):
        root = Node(value, left=root)
    return root
