"""
This module provides various functions for testing.

Functions:
    * test_add: Performs test on the function add.
"""

import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))  # noqa
import module as m  # noqa


def test_add():
    """
    Test the add_numbers function.

    This function checks if the add_numbers function
    produces the expected results.
    """
    assert m.add(1, 2) == 3
    assert m.add(0, 0) == 0
    assert m.add(-1, 1) == 0
    assert m.add(-1, -1) == -2


if __name__ == "__main__":
    pytest.main()
