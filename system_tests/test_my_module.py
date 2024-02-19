import sys
import pytest
from system_tests import add
sys.path.append('../system_tests')


def test_add_numbers():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


if __name__ == "__main__":
    pytest.main()
