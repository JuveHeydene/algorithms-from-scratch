from binary_tree import Node, left_chain, sample_tree
from level_order import level_order, levels, right_side_view


class TestLevelOrder:
    def test_empty_tree(self):
        assert level_order(None) == []

    def test_single_node(self):
        assert level_order(Node(42)) == [42]

    def test_sample_tree(self):
        assert level_order(sample_tree()) == list("FBGADICEH")

    def test_complete_tree(self):
        tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        assert level_order(tree) == [1, 2, 3, 4, 5, 6, 7]

    def test_very_deep_tree(self):
        assert level_order(left_chain(10_000)) == list(range(10_000))

    def test_does_not_modify_the_tree(self):
        tree = sample_tree()
        level_order(tree)
        assert tree == sample_tree()


class TestLevels:
    def test_empty_tree(self):
        assert levels(None) == []

    def test_sample_tree(self):
        assert levels(sample_tree()) == [["F"], ["B", "G"], ["A", "D", "I"], ["C", "E", "H"]]

    def test_one_node_per_level(self):
        assert levels(left_chain(3)) == [[0], [1], [2]]


class TestRightSideView:
    def test_empty_tree(self):
        assert right_side_view(None) == []

    def test_sample_tree(self):
        assert right_side_view(sample_tree()) == ["F", "G", "I", "H"]

    def test_left_node_visible_when_nothing_on_its_right(self):
        tree = Node(1, left=Node(2, left=Node(4)), right=Node(3))
        assert right_side_view(tree) == [1, 3, 4]
