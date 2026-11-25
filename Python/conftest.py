"""Make every algorithm family importable from the tests.

The folders are numbered (``01_tree_traversal``), and a Python module name
cannot start with a digit, so the families cannot be regular packages.
Instead, each family folder is added to ``sys.path``: that way a test can write
``from binary_tree import Node`` to reach the structure shared by its family.

pytest already adds the folder of each test file to ``sys.path``, so a test can
also write ``from preorder import preorder`` to reach the code next to it.
Consequence: every ``.py`` file name must be unique across the whole project.
"""

import sys
from pathlib import Path

SRC = Path(__file__).parent / "src"

for family in sorted(SRC.iterdir()):
    if family.is_dir() and not family.name.startswith((".", "_")):
        sys.path.insert(0, str(family))
