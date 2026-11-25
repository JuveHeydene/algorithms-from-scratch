# Algorithms in Python

The Python implementation of the [catalog](../README.md). Each algorithm folder holds a full course (`README.md`), the code, and its tests.

## Setup

Requirements: Python 3.12+.

```bash
cd Python
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Running the tests

```bash
pytest                    # everything
pytest -k preorder        # one algorithm (matches file, class and test names)
pytest src/01_tree_traversal
pytest -x                 # stop at the first failure
```

## How I work on an algorithm

1. Read the family course (`src/<family>/README.md`), then the algorithm's course.
2. Run its tests and watch them fail: every function starts as `raise NotImplementedError`.
3. Implement it from scratch, without looking anything up and without library shortcuts (`sorted`, `heapq`, graph libraries…). The standard containers (`list`, `dict`, `set`, `collections.deque`) are fine.
4. Make every test green, then move to the next algorithm.

## Layout

```
Python/
├── conftest.py                  # puts every family folder on the import path
├── pyproject.toml               # pytest settings
├── requirements-dev.txt
└── src/
    ├── 01_tree_traversal/
    │   ├── README.md            # the course for the whole family
    │   ├── binary_tree.py       # Node + sample trees, shared by the family
    │   ├── assets/              # figures of the family course
    │   ├── 01_preorder/
    │   │   ├── README.md        # the course for this algorithm
    │   │   ├── preorder.py      # what I implement
    │   │   ├── test_preorder.py
    │   │   └── assets/
    │   ├── 02_inorder/
    │   ├── 03_postorder/
    │   └── 04_level_order/
    └── 02_graph_traversal/
        ├── README.md
        ├── graph.py             # adjacency list type + sample graphs
        ├── 01_bfs/
        └── 02_dfs/
```

### Conventions

- Folder names start with a number to keep the reading order. A Python module name cannot start with a digit, so the folders are not packages: [conftest.py](conftest.py) adds each family folder to the import path, and pytest adds each test's own folder. Tests simply write `from binary_tree import Node` and `from preorder import preorder`.
- Because of that, **every `.py` file name must be unique** across the project.
- Code, comments and documentation are in English.
