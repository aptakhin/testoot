import pytest

from testoot.ext.pytest import PytestContext
from testoot.testoot import Testoot


@pytest.fixture(scope='module')
def base_testoot(root_base_testoot):
    testoot = root_base_testoot.clone(
        storage=root_base_testoot.storage.clone(add_path='examples'),
    )
    testoot.storage.ensure_exists()
    yield testoot

@pytest.fixture(scope='function')
def testoot(base_testoot, request):
    testoot = Testoot(base_testoot, PytestContext(request))
    yield testoot
