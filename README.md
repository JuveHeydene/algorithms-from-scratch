# Algorithms

A hands-on implementation of the **classic algorithms of computer science** in **Python** and **C++**, each one backed by unit tests.

The goal of this repository is to learn each algorithm by writing it from scratch: what problem it solves, how it works step by step, what it costs in time and memory, and how to prove it is correct.

No shortcuts: I don't use `sorted()`, `std::sort`, `heapq` or a graph library to implement the algorithm itself. They are only allowed inside tests, to check my results.

---

## Why algorithms matter

An algorithm is a **finite sequence of well-defined steps that solves a problem**. Data structures say how information is stored; algorithms say what we do with it.

Writing them by hand matters for several reasons:

- **Thinking in complexity.** Knowing that one approach is `O(n²)` and another is `O(n log n)` is the difference between a program that answers in a second and one that never finishes.
- **Recognising problem shapes.** Many real problems are classic ones in disguise: a dependency graph is a topological sort, a GPS route is a shortest path, a project schedule is PERT / critical path.
- **Understanding the tools I already use.** Standard library sorts, database indexes, network routing and package managers are all built on these algorithms.
- **Technical interviews and competitive programming.** Traversals, shortest paths, dynamic programming and sorting come up again and again.
- **Knowing the trade-offs.** Stable or not, in-place or not, works with negative weights or not. Each algorithm has a domain where it shines and one where it breaks.

---

## Languages

| Language | Why |
| --- | --- |
| **Python** | Reads almost like pseudocode, so the logic of the algorithm stays in front. It is the standard language for interviews and teaching, and `pytest` makes testing quick. |
| **C++** | Puts me close to memory: arrays, pointers, references, the cost of every copy. It is the reference language for competitive programming, and the STL (Standard Template Library: `vector`, `priority_queue`, `unordered_map`) maps directly onto the data structures the algorithms need. |

Writing each algorithm twice is the point: Python to get the idea right, C++ to understand what really happens underneath. I start with Python; the C++ side follows once a family is done.

---

## Catalog & progress

✅ implemented with tests · 🟡 course and tests ready, implementation in progress · ⬜ not started

Each family links to a full course that explains the algorithms from zero, with figures, step-by-step traces, complexity and real-world uses.

Complexities are given for the usual implementation. `n` = number of elements, `V` = vertices, `E` = edges.

### 1. Tree traversal

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | [Preorder](Python/src/01_tree_traversal/01_preorder/) | Node, then left subtree, then right subtree. Copies and prints hierarchies. | `O(n)` | 🟡 | ⬜ |
| 02 | [Inorder](Python/src/01_tree_traversal/02_inorder/) | Left subtree, then node, then right subtree. Gives a binary search tree in sorted order. | `O(n)` | 🟡 | ⬜ |
| 03 | [Postorder](Python/src/01_tree_traversal/03_postorder/) | Left subtree, then right subtree, then node. Combines children's results (sizes, evaluation). | `O(n)` | 🟡 | ⬜ |
| 04 | [Level order](Python/src/01_tree_traversal/04_level_order/) | Level by level with a queue. Breadth-first search on a tree. | `O(n)` | 🟡 | ⬜ |

### 2. Graph traversal

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | [Breadth-First Search (BFS)](Python/src/02_graph_traversal/01_bfs/) | Explore the graph level by level using a queue. Finds shortest paths in unweighted graphs. | `O(V + E)` | 🟡 | ⬜ |
| 02 | [Depth-First Search (DFS)](Python/src/02_graph_traversal/02_dfs/) | Go as deep as possible before backtracking, using a stack or recursion. | `O(V + E)` | 🟡 | ⬜ |
| 03 | Cycle detection | Use DFS colours (white / grey / black) or Union-Find to find a cycle. | `O(V + E)` | ⬜ | ⬜ |
| 04 | Connected components | Group vertices that can reach each other, with BFS or DFS. | `O(V + E)` | ⬜ | ⬜ |
| 05 | Bipartite check | Try to 2-colour the graph with BFS. | `O(V + E)` | ⬜ | ⬜ |
| 06 | Topological sort (Kahn / DFS) | Order the vertices of a directed acyclic graph (DAG: arrows, no loops) so every edge goes forward. | `O(V + E)` | ⬜ | ⬜ |
| 07 | Strongly connected components (Tarjan / Kosaraju) | Find the maximal groups of vertices that all reach each other in a directed graph. | `O(V + E)` | ⬜ | ⬜ |

### 3. Shortest paths

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | Dijkstra | Greedy expansion from the source with a priority queue. Non-negative weights only. | `O((V + E) log V)` | ⬜ | ⬜ |
| 02 | Bellman-Ford | Relax every edge `V - 1` times. Handles negative weights and detects negative cycles. | `O(V · E)` | ⬜ | ⬜ |
| 03 | Floyd-Warshall | Dynamic programming over all pairs of vertices. | `O(V³)` | ⬜ | ⬜ |
| 04 | A* | Dijkstra guided by a heuristic towards the target. | depends on heuristic | ⬜ | ⬜ |

### 4. Minimum spanning tree

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | Kruskal | Sort edges by weight and add them if they don't create a cycle (Union-Find). | `O(E log E)` | ⬜ | ⬜ |
| 02 | Prim | Grow the tree from one vertex, always taking the cheapest outgoing edge. | `O((V + E) log V)` | ⬜ | ⬜ |

### 5. Scheduling & flows

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | PERT | Compute earliest / latest start dates and slack of tasks in a project graph. | `O(V + E)` | ⬜ | ⬜ |
| 02 | Critical Path Method (CPM) | Find the longest path in the task graph: the tasks that cannot be delayed. | `O(V + E)` | ⬜ | ⬜ |
| 03 | Ford-Fulkerson / Edmonds-Karp | Push flow along augmenting paths (found with BFS) until none is left. | `O(V · E²)` | ⬜ | ⬜ |

### 6. Sorting

| # | Algorithm | Idea | Best | Average | Worst | Stable | Python | C++ |
| --- | --- | --- | --- | --- | --- | :---: | :---: | :---: |
| 01 | Bubble sort | Swap adjacent elements until nothing moves. | `O(n)` | `O(n²)` | `O(n²)` | yes | ⬜ | ⬜ |
| 02 | Selection sort | Repeatedly pick the minimum and put it in place. | `O(n²)` | `O(n²)` | `O(n²)` | no | ⬜ | ⬜ |
| 03 | Insertion sort | Insert each element into the sorted prefix. | `O(n)` | `O(n²)` | `O(n²)` | yes | ⬜ | ⬜ |
| 04 | Merge sort | Split in two, sort each half, merge. | `O(n log n)` | `O(n log n)` | `O(n log n)` | yes | ⬜ | ⬜ |
| 05 | Quick sort | Partition around a pivot, recurse on each side. | `O(n log n)` | `O(n log n)` | `O(n²)` | no | ⬜ | ⬜ |
| 06 | Heap sort | Build a max-heap, extract the max repeatedly. | `O(n log n)` | `O(n log n)` | `O(n log n)` | no | ⬜ | ⬜ |
| 07 | Shell sort | Insertion sort on elements spaced by a shrinking gap. | `O(n log n)` | gap-dependent | `O(n²)` | no | ⬜ | ⬜ |
| 08 | Counting sort | Count occurrences of each key (small integer range). | `O(n + k)` | `O(n + k)` | `O(n + k)` | yes | ⬜ | ⬜ |
| 09 | Radix sort | Sort digit by digit with a stable sort. | `O(d · (n + k))` | `O(d · (n + k))` | `O(d · (n + k))` | yes | ⬜ | ⬜ |
| 10 | Bucket sort | Spread elements into buckets, sort each bucket. | `O(n + k)` | `O(n + k)` | `O(n²)` | yes | ⬜ | ⬜ |

### 7. Searching

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | Linear search | Check every element one by one. | `O(n)` | ⬜ | ⬜ |
| 02 | Binary search | Halve a sorted interval at each step. | `O(log n)` | ⬜ | ⬜ |
| 03 | Ternary search | Find the extremum of a unimodal function. | `O(log n)` | ⬜ | ⬜ |
| 04 | Quickselect | Find the k-th smallest element with quick sort's partition. | `O(n)` average | ⬜ | ⬜ |

### 8. Dynamic programming

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | Fibonacci (memo / tabulation) | The simplest example of overlapping subproblems. | `O(n)` | ⬜ | ⬜ |
| 02 | 0/1 Knapsack | Maximise value under a weight limit. | `O(n · W)` | ⬜ | ⬜ |
| 03 | Longest Common Subsequence | Longest sequence present in two strings, in order. | `O(n · m)` | ⬜ | ⬜ |
| 04 | Edit distance (Levenshtein) | Minimum insertions, deletions and substitutions between two strings. | `O(n · m)` | ⬜ | ⬜ |
| 05 | Longest Increasing Subsequence | Longest strictly increasing subsequence. | `O(n log n)` | ⬜ | ⬜ |
| 06 | Coin change | Minimum coins / number of ways to reach an amount. | `O(n · amount)` | ⬜ | ⬜ |

### 9. Greedy & backtracking

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | Activity selection | Always pick the activity that ends first. | `O(n log n)` | ⬜ | ⬜ |
| 02 | Huffman coding | Build an optimal prefix code by merging the two rarest symbols. | `O(n log n)` | ⬜ | ⬜ |
| 03 | N-Queens | Place queens one row at a time, backtrack on conflict. | `O(n!)` | ⬜ | ⬜ |
| 04 | Sudoku solver | Fill cells and undo choices that lead to a dead end. | exponential | ⬜ | ⬜ |

### 10. Strings

| # | Algorithm | Idea | Time | Python | C++ |
| --- | --- | --- | --- | :---: | :---: |
| 01 | Naive pattern matching | Try the pattern at every position. | `O(n · m)` | ⬜ | ⬜ |
| 02 | Knuth-Morris-Pratt (KMP) | Use a failure table to never re-read the text. | `O(n + m)` | ⬜ | ⬜ |
| 03 | Rabin-Karp | Compare rolling hashes instead of characters. | `O(n + m)` average | ⬜ | ⬜ |

### 11. Supporting data structures

These are not algorithms on their own, but several algorithms above depend on them, so I implement them too.

| # | Structure | Used by | Python | C++ |
| --- | --- | --- | :---: | :---: |
| 01 | Graph (adjacency list / matrix) | every graph algorithm | ⬜ | ⬜ |
| 02 | Binary heap / priority queue | Dijkstra, Prim, Heap sort, Huffman | ⬜ | ⬜ |
| 03 | Union-Find (Disjoint Set Union) | Kruskal, cycle detection | ⬜ | ⬜ |

---

## Repository structure

Both implementations follow the same numbered layout, so an algorithm is easy to find in either language. Each algorithm sits next to its test and its course.

```
Algorithme/
├── Python/                               # Python 3.12+, pytest
│   ├── conftest.py
│   ├── pyproject.toml
│   └── src/
│       ├── 01_tree_traversal/
│       │   ├── README.md                 # course for the whole family
│       │   ├── binary_tree.py            # structure shared by the family
│       │   ├── assets/                   # SVG figures
│       │   ├── 01_preorder/
│       │   │   ├── README.md             # course for this algorithm
│       │   │   ├── preorder.py
│       │   │   └── test_preorder.py
│       │   ├── 02_inorder/
│       │   ├── 03_postorder/
│       │   └── 04_level_order/
│       ├── 02_graph_traversal/
│       │   ├── 01_bfs/
│       │   └── 02_dfs/
│       ├── 03_shortest_paths/
│       ├── 04_minimum_spanning_tree/
│       ├── 05_scheduling_and_flows/
│       ├── 06_sorting/
│       ├── 07_searching/
│       ├── 08_dynamic_programming/
│       ├── 09_greedy_and_backtracking/
│       ├── 10_strings/
│       └── 11_data_structures/
│
└── Cpp/                                  # C++20, CMake, GoogleTest (coming later)
    ├── CMakeLists.txt
    └── src/                              # same layout as Python/
```

Each **family** folder has a `README.md` that teaches the whole family from zero: analogies, vocabulary, figures, the shared theory and how the algorithms compare. Each **algorithm** folder has its own `README.md`: intuition, step-by-step trace, recursive and iterative versions, complexity, real-world uses, common mistakes, a checkpoint quiz and the exercises.

---

## Running the tests

### Python

Requirements: Python 3.12+.

```bash
cd Python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest                # all tests
pytest -k preorder    # only one algorithm
```

More details in [Python/README.md](Python/README.md).

### C++

Requirements: a C++20 compiler (GCC 11+ or Clang 14+) and CMake 3.20+. GoogleTest is fetched automatically by CMake.

```bash
cd Cpp
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

---

## References

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (CLRS), MIT Press, 4th edition, 2022.
- Sedgewick & Wayne, *Algorithms*, Addison-Wesley, 4th edition, 2011.
- Halim & Halim, *Competitive Programming 4*, 2020.
- [VisuAlgo](https://visualgo.net): animated visualisations of most algorithms listed here.
- [CP-Algorithms](https://cp-algorithms.com): detailed explanations with C++ implementations.
