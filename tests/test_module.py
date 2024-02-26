"""
This module provides various functions for testing.

Functions:
    * test_add: Performs test on the function add.
"""

import pytest
from .src import module


def test_add():
    """
    Test the add_numbers function.

    This function checks if the add_numbers function produces the expected results.
    """
    assert module.add(1, 2) == 3
    assert module.add(0, 0) == 0
    assert module.add(-1, 1) == 0
    assert module.add(-1, -1) == -2


if __name__ == "__main__":
    pytest.main()
