import pytest

from binary_tree import Node, expression_tree, left_chain, sample_tree
from postorder import evaluate, height, postorder, postorder_iterative

TRAVERSALS = [postorder, postorder_iterative]


@pytest.mark.parametrize("traverse", TRAVERSALS)
class TestPostorder:
    def test_empty_tree(self, traverse):
        assert traverse(None) == []

    def test_single_node(self, traverse):
        assert traverse(Node(42)) == [42]

    def test_sample_tree(self, traverse):
        assert traverse(sample_tree()) == list("ACEDBHIGF")

    def test_root_always_comes_last(self, traverse):
        tree = sample_tree()
        assert traverse(tree)[-1] == tree.value

    def test_only_right_children(self, traverse):
        tree = Node(1, right=Node(2, right=Node(3)))
        assert traverse(tree) == [3, 2, 1]

    def test_does_not_modify_the_tree(self, traverse):
        tree = sample_tree()
        traverse(tree)
        assert tree == sample_tree()


def test_iterative_survives_a_very_deep_tree():
    assert postorder_iterative(left_chain(10_000)) == list(reversed(range(10_000)))


class TestEvaluate:
    def test_expression(self):
        assert evaluate(expression_tree()) == 21

    def test_single_number(self):
        assert evaluate(Node(7)) == 7

    def test_division_and_subtraction_keep_their_order(self):
        # (8 - 2) / 4 = 1.5  (not 2 - 8, not 4 / 6)
        tree = Node("/", left=Node("-", left=Node(8), right=Node(2)), right=Node(4))
        assert evaluate(tree) == pytest.approx(1.5)


class TestHeight:
    def test_empty(self):
        assert height(None) == 0

    def test_single_node(self):
        assert height(Node(1)) == 1

    def test_sample_tree(self):
        assert height(sample_tree()) == 4

    def test_degenerate_tree(self):
        assert height(left_chain(50)) == 50
