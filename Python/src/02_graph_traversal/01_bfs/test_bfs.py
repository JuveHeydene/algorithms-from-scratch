from bfs import bfs, bfs_distances, shortest_path
from graph import chain_graph, sample_graph


def is_valid_path(graph, path):
    return all(b in graph.get(a, []) for a, b in zip(path, path[1:]))


class TestBfs:
    def test_sample_graph(self):
        assert bfs(sample_graph(), "A") == list("ABEDCGF")

    def test_starting_somewhere_else(self):
        assert bfs(sample_graph(), "F") == list("FDBCAEG")

    def test_each_vertex_appears_once_despite_the_cycle(self):
        order = bfs(sample_graph(), "A")
        assert sorted(order) == sorted(set(order)) == list("ABCDEFG")

    def test_isolated_vertex(self):
        assert bfs({"X": []}, "X") == ["X"]

    def test_unreachable_part_is_ignored(self):
        graph = {"A": ["B"], "B": ["A"], "Z": ["Y"], "Y": ["Z"]}
        assert bfs(graph, "A") == ["A", "B"]

    def test_directed_graph_follows_arrows_only(self):
        graph = {"A": ["B"], "B": ["C"], "C": []}
        assert bfs(graph, "B") == ["B", "C"]

    def test_vertex_that_is_never_a_key(self):
        assert bfs({"A": ["B"]}, "A") == ["A", "B"]

    def test_long_chain(self):
        assert bfs(chain_graph(10_000), 0) == list(range(10_000))


class TestBfsDistances:
    def test_sample_graph(self):
        assert bfs_distances(sample_graph(), "A") == {
            "A": 0, "B": 1, "E": 1, "D": 2, "C": 2, "G": 2, "F": 3,
        }

    def test_unreachable_vertices_are_absent(self):
        assert bfs_distances({"A": [], "B": ["A"]}, "A") == {"A": 0}


class TestShortestPath:
    def test_sample_graph(self):
        assert shortest_path(sample_graph(), "A", "F") == ["A", "B", "D", "F"]

    def test_path_is_valid_and_minimal(self):
        graph = sample_graph()
        path = shortest_path(graph, "G", "B")
        assert path[0] == "G" and path[-1] == "B"
        assert is_valid_path(graph, path)
        assert len(path) - 1 == bfs_distances(graph, "G")["B"]

    def test_start_equals_goal(self):
        assert shortest_path(sample_graph(), "C", "C") == ["C"]

    def test_unreachable_goal(self):
        assert shortest_path({"A": ["B"], "B": [], "C": []}, "A", "C") is None

    def test_prefers_fewer_edges_over_list_order(self):
        # The long way is listed first, BFS must still find the direct edge.
        graph = {"S": ["X", "T"], "X": ["Y"], "Y": ["T"], "T": []}
        assert shortest_path(graph, "S", "T") == ["S", "T"]
