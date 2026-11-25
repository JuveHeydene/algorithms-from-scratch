import pytest

from binary_tree import Node, expression_tree, left_chain, sample_tree
from preorder import preorder, preorder_iterative, to_prefix

TRAVERSALS = [preorder, preorder_iterative]


@pytest.mark.parametrize("traverse", TRAVERSALS)
class TestPreorder:
    def test_empty_tree(self, traverse):
        assert traverse(None) == []

    def test_single_node(self, traverse):
        assert traverse(Node(42)) == [42]

    def test_sample_tree(self, traverse):
        assert traverse(sample_tree()) == list("FBADCEGIH")

    def test_root_always_comes_first(self, traverse):
        tree = sample_tree()
        assert traverse(tree)[0] == tree.value

    def test_only_right_children(self, traverse):
        tree = Node(1, right=Node(2, right=Node(3)))
        assert traverse(tree) == [1, 2, 3]

    def test_does_not_modify_the_tree(self, traverse):
        tree = sample_tree()
        traverse(tree)
        assert tree == sample_tree()


def test_iterative_survives_a_very_deep_tree():
    # 10,000 levels: far beyond Python's default recursion limit (1,000).
    assert preorder_iterative(left_chain(10_000)) == list(range(10_000))


class TestToPrefix:
    def test_expression(self):
        assert to_prefix(expression_tree()) == "* + 3 4 - 5 2"

    def test_single_number(self):
        assert to_prefix(Node(7)) == "7"

    def test_empty(self):
        assert to_prefix(None) == ""
