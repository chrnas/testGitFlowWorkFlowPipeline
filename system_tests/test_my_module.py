import sys
import pytest
from testGitFlowWorkFlowPipeline import my_module
from my_module import add
sys.path.append('../testGitFlowWorkFlowPipeline')


def test_add_numbers():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


if __name__ == "__main__":
    pytest.main()
