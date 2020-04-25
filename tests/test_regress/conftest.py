import pytest

from regress.ext.pytest import PytestContext
from regress.fixture import RegressFixture
from regress.impl.run_policy.ask_canonize_policy import AskCanonizePolicy
from regress.impl.serializer.json_serializer import JsonSerializer
from regress.impl.storage.local_directory_storage import LocalDirectoryStorage
from regress.impl.user_interaction.constant_interaction import \
    ConstantUserInteraction
from regress.regress import Regress


class TestRegress(Regress):
    """Test regress"""
    def __init__(self):
        super().__init__(
            storage=LocalDirectoryStorage('.regress', mode='t'),
            serializer=JsonSerializer(),
            run_policy=AskCanonizePolicy(
                ConstantUserInteraction(canonize=False),
            ),
        )

    def ensure_exists(self, clear=False):
        return self._storage.ensure_exists(clear=clear)


@pytest.fixture(scope='module')
def test_regress_instance():
    regress = TestRegress()
    regress.ensure_exists(clear=True)
    yield regress


@pytest.fixture(scope='function')
def test_regress(test_regress_instance, request):
    fixture = RegressFixture(test_regress_instance, PytestContext(request))
    yield fixture
