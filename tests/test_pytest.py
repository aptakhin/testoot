import pytest

from regress.ext.pytest import PytestContext
from regress.fixture import RegressFixture
from regress.impl.run_policy.ask_canonize_policy import AskCanonizePolicy
from regress.impl.serializer.json_serializer import JsonSerializer
from regress.impl.storage.local_directory_storage import LocalDirectoryStorage
from regress.impl.user_interaction.console_user_interaction import \
    ConsoleUserInteraction
from regress.regress import Regress


class ConsoleTestRegress(Regress):
    """Test regress"""
    def __init__(self):
        super().__init__(
            storage=LocalDirectoryStorage('.regress', mode='t'),
            serializer=JsonSerializer(),
            run_policy=AskCanonizePolicy(ConsoleUserInteraction()),
        )

    def ensure_exists(self, clear=False):
        return self._storage.ensure_exists(clear=clear)


@pytest.fixture(scope='module')
def console_regress_instance():
    regress = ConsoleTestRegress()
    regress.ensure_exists(clear=True)
    yield regress


@pytest.fixture(scope='function')
def console_regress(console_regress_instance, request):
    fixture = RegressFixture(console_regress_instance, PytestContext(request))
    yield fixture


@pytest.mark.skip
def test_simple(console_regress: RegressFixture):
    result = {'a': 1}
    console_regress.test(result)  # Commit

    result3 = {'a': 2}  # Try commit change
    console_regress.test(result3)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
