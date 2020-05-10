import pytest

from testoot.ext.pytest import PytestContext
from testoot.pub import \
    AskCanonizePolicy, ConstantUserInteraction
from testoot.testoot import Testoot
from testoot.serializers import JsonSerializer


@pytest.fixture(scope='module')
def base_testoot(root_base_testoot):
    testoot = root_base_testoot.clone(
        storage=root_base_testoot.storage.clone(add_path='canonize'),
        serializer=JsonSerializer(),
        canonize_policy=AskCanonizePolicy(
            ConstantUserInteraction(canonize=False),
        ),
    )
    testoot.storage.ensure_exists()
    yield testoot


class CanonizeTestoot(Testoot):
    def __init__(self, regress_base, context):
        super().__init__(regress_base, context)

    def set_canonize(self, canonize):
        self.canonize_policy._user_interaction.canonize = canonize


@pytest.fixture(scope='function')
def testoot(base_testoot, request):
    testoot = CanonizeTestoot(base_testoot,
                              PytestContext(request, ask_canonize=True))
    yield testoot
