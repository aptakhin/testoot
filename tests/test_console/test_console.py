import pytest

from testoot.testoot import Testoot


@pytest.mark.canonize
def test_simple(testoot: Testoot):
    result = {'a': 1}
    testoot.test(result)  # Commit

    result2 = {'a': 2}  # Try commit change
    testoot.test(result2)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
