import pytest

from dfs import dfs, dfs_iterative, find_path
from graph import chain_graph, sample_graph

TRAVERSALS = [dfs, dfs_iterative]


def is_valid_path(graph, path):
    return all(b in graph.get(a, []) for a, b in zip(path, path[1:]))


@pytest.mark.parametrize("traverse", TRAVERSALS)
class TestDfs:
    def test_sample_graph(self, traverse):
        assert traverse(sample_graph(), "A") == list("ABDCEGF")

    def test_starting_somewhere_else(self, traverse):
        assert traverse(sample_graph(), "G") == list("GEABDCF")

    def test_each_vertex_appears_once_despite_the_cycle(self, traverse):
        order = traverse(sample_graph(), "A")
        assert sorted(order) == sorted(set(order)) == list("ABCDEFG")

    def test_isolated_vertex(self, traverse):
        assert traverse({"X": []}, "X") == ["X"]

    def test_unreachable_part_is_ignored(self, traverse):
        graph = {"A": ["B"], "B": ["A"], "Z": ["Y"], "Y": ["Z"]}
        assert traverse(graph, "A") == ["A", "B"]

    def test_directed_graph_follows_arrows_only(self, traverse):
        graph = {"A": ["B"], "B": ["C"], "C": []}
        assert traverse(graph, "B") == ["B", "C"]

    def test_vertex_that_is_never_a_key(self, traverse):
        assert traverse({"A": ["B"]}, "A") == ["A", "B"]

    def test_goes_deep_before_wide(self, traverse):
        graph = {"R": ["X", "Y"], "X": ["X1"], "X1": [], "Y": []}
        assert traverse(graph, "R") == ["R", "X", "X1", "Y"]


def test_iterative_survives_a_very_long_chain():
    assert dfs_iterative(chain_graph(10_000), 0) == list(range(10_000))


class TestFindPath:
    def test_sample_graph(self):
        assert find_path(sample_graph(), "A", "F") == ["A", "B", "D", "F"]

    def test_not_necessarily_the_shortest(self):
        # BFS would answer A -> E -> C (2 edges). DFS dives through B first.
        assert find_path(sample_graph(), "A", "C") == ["A", "B", "D", "C"]

    def test_path_is_valid(self):
        graph = sample_graph()
        path = find_path(graph, "G", "F")
        assert path[0] == "G" and path[-1] == "F"
        assert is_valid_path(graph, path)
        assert len(path) == len(set(path))

    def test_start_equals_goal(self):
        assert find_path(sample_graph(), "C", "C") == ["C"]

    def test_unreachable_goal(self):
        assert find_path({"A": ["B"], "B": [], "C": []}, "A", "C") is None
