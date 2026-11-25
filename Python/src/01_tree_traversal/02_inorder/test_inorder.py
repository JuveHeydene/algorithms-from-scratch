import pytest

from binary_tree import Node, expression_tree, left_chain, sample_tree
from inorder import inorder, inorder_iterative, is_binary_search_tree, to_infix

TRAVERSALS = [inorder, inorder_iterative]


@pytest.mark.parametrize("traverse", TRAVERSALS)
class TestInorder:
    def test_empty_tree(self, traverse):
        assert traverse(None) == []

    def test_single_node(self, traverse):
        assert traverse(Node(42)) == [42]

    def test_sample_tree_comes_out_sorted(self, traverse):
        assert traverse(sample_tree()) == list("ABCDEFGHI")

    def test_only_right_children(self, traverse):
        tree = Node(1, right=Node(2, right=Node(3)))
        assert traverse(tree) == [1, 2, 3]

    def test_only_left_children(self, traverse):
        tree = Node(3, left=Node(2, left=Node(1)))
        assert traverse(tree) == [1, 2, 3]

    def test_does_not_modify_the_tree(self, traverse):
        tree = sample_tree()
        traverse(tree)
        assert tree == sample_tree()


def test_iterative_survives_a_very_deep_tree():
    # left_chain: root 0, deepest leaf 9,999 -> inorder starts from the bottom.
    assert inorder_iterative(left_chain(10_000)) == list(reversed(range(10_000)))


class TestToInfix:
    def test_expression(self):
        assert to_infix(expression_tree()) == "((3 + 4) * (5 - 2))"

    def test_single_number(self):
        assert to_infix(Node(7)) == "7"

    def test_empty(self):
        assert to_infix(None) == ""


class TestIsBinarySearchTree:
    def test_sample_tree_is_a_bst(self):
        assert is_binary_search_tree(sample_tree()) is True

    def test_empty_tree_is_a_bst(self):
        assert is_binary_search_tree(None) is True

    def test_wrong_child_order(self):
        assert is_binary_search_tree(Node(5, left=Node(8), right=Node(2))) is False

    def test_violation_deep_in_the_tree(self):
        # Every parent/child pair looks fine, but 6 sits in the LEFT subtree of 5.
        tree = Node(5, left=Node(3, right=Node(6)), right=Node(8))
        assert is_binary_search_tree(tree) is False

    def test_duplicates_are_not_allowed(self):
        assert is_binary_search_tree(Node(5, left=Node(5))) is False
