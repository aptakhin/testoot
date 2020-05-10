import pytest

from testoot.ext.pytest import PytestContext
from testoot.pub import AskCanonizePolicy
from testoot.testoot import Testoot
from testoot.serializers import JsonSerializer
from testoot.user_interactions import ConsoleUserInteraction


@pytest.fixture(scope='module')
def base_testoot(root_base_testoot):
    testoot = root_base_testoot.clone(
        storage=root_base_testoot.storage.clone(add_path='console'),
        serializer=JsonSerializer(),
        canonize_policy=AskCanonizePolicy(
            ConsoleUserInteraction(),
        ),
    )
    testoot.storage.ensure_exists()
    yield testoot


@pytest.fixture(scope='function')
def testoot(base_testoot, request):
    testoot = Testoot(base_testoot, PytestContext(request))
    yield testoot
