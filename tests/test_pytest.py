import pytest

from regress.ext.pytest import PytestContext
from regress.ext.simple import LocalRegress
from regress.fixture import RegressFixture


@pytest.fixture(scope='module')
def regress_instance():
    regress = LocalRegress()
    regress.ensure_exists(clear=True)
    yield regress


@pytest.fixture(scope='function')
def regress(regress_instance, request):
    fixture = RegressFixture(regress_instance, PytestContext(request))
    yield fixture


def test_simple(regress: RegressFixture):
    result = {'a': 1}
    regress.test(result)  # Commit

    result2 = {'a': 1}
    regress.test(result2)  # No changes

    result3 = {'a': 2}  # Try commit change
    with pytest.raises(AssertionError) as e:
        regress.test(result3)


def test_simple_duplicate(regress: RegressFixture):
    result = {'a': 1}
    regress.test(result)  # Commit

    result2 = {'a': 1}
    regress.test(result2)  # No changes

    result3 = {'a': 2}  # Try commit change
    with pytest.raises(AssertionError) as e:
        regress.test(result3)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
