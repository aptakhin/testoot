import pytest

from src.regress.ext.pytest import RegressFixture
from src.regress.ext.simple import LocalRegress


@pytest.fixture(scope='module')
def local_regress_instance():
    regress = LocalRegress()
    regress.ensure_exists(clear=True)
    yield regress


@pytest.fixture(scope='function')
def local_regress(local_regress_instance, request):
    fixture = RegressFixture(local_regress_instance, request)
    yield fixture


def test_simple(local_regress: RegressFixture):
    result = {'a': 1}
    local_regress.test(result)  # Commit

    local_regress.test(result)  # No changes

    result2 = {'a': 2}  # Try commit change
    with pytest.raises(AssertionError) as e:
        local_regress.test(result2)


def test_simple2(local_regress: RegressFixture):
    result = {'a': 2}
    local_regress.test(result)  # Commit

    local_regress.test(result)  # No changes

    result2 = {'a': 3}  # Try commit change
    with pytest.raises(AssertionError) as e:
        local_regress.test(result2)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
