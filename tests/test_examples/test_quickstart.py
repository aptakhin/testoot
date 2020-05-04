# region: header
import pytest

from regress.ext.pytest import PytestContext, register_addoption
from regress.regress import Regress
from regress.pub import DefaultBaseRegress


def pytest_addoption(parser):
    register_addoption(parser)


@pytest.fixture(scope='module')
def regress_instance():
    regress = DefaultBaseRegress()
    regress.storage.ensure_exists()
    yield regress


@pytest.fixture(scope='function')
def regress(regress_instance, request):
    fixture = Regress(regress_instance,
                      PytestContext(request))
    yield fixture
# endregion: header

@pytest.mark.no_canonize  # Here for not including to docs page
# region: test_simple
# regress is the helper fixture easy to setup
def test_simple(regress: Regress):
    result = {'a': 1}
    regress.test(result)  # Commit first time

    result2 = {'a': 1}
    regress.test(result2)  # Ok. No object result changes

    result3 = {'a': 3}  # Try commit change. Raised the AssertionError
    with pytest.raises(AssertionError) as e:
        regress.test(result3)
# endregion: test_simple
