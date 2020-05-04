import pytest

from regress.ext.pytest import PytestContext
from regress.pub import AskCanonizePolicy
from regress.regress import Regress
from regress.serializers import JsonSerializer
from regress.user_interactions import ConsoleUserInteraction


@pytest.fixture(scope='module')
def base_regress(root_base_regress):
    regress = root_base_regress.clone(
        storage=root_base_regress.storage.clone(add_path='console'),
        serializer=JsonSerializer(),
        canonize_policy=AskCanonizePolicy(
            ConsoleUserInteraction(),
        ),
    )
    regress.storage.ensure_exists()
    yield regress


@pytest.fixture(scope='function')
def regress(base_regress, request):
    regress = Regress(base_regress, PytestContext(request))
    yield regress
