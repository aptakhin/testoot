# region: header
import pytest

from testoot.ext.pytest import PytestContext, register_addoption
from testoot.testoot import Testoot
from testoot.pub import DefaultBaseTestoot


def pytest_addoption(parser):
    register_addoption(parser)


@pytest.fixture(scope='module')
def testoot_instance():
    testoot = DefaultBaseTestoot()
    testoot.storage.ensure_exists()
    yield testoot


@pytest.fixture(scope='function')
def testoot(testoot_instance, request):
    fixture = Testoot(testoot_instance,
                      PytestContext(request))
    yield fixture
# endregion: header

@pytest.mark.no_canonize  # Here for not including to docs page
# region: test_simple
# regress is the helper fixture easy to setup
def test_simple(testoot: Testoot):
    result = {'a': 1}
    testoot.test(result)  # Commit first time

    result2 = {'a': 1}
    testoot.test(result2)  # Ok. No object result changes

    result3 = {'a': 3}  # Try commit change. Raised the AssertionError
    with pytest.raises(AssertionError) as e:
        testoot.test(result3)
# endregion: test_simple
