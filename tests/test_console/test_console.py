import pytest

from regress.regress import Regress


@pytest.mark.canonize
def test_simple(regress: Regress):
    result = {'a': 1}
    regress.test(result)  # Commit

    result2 = {'a': 2}  # Try commit change
    regress.test(result2)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
