import pytest

from regress.ext.pytest import PytestContext
from regress.ext.simple import DefaultBaseRegress
from regress.regress import Regress
from regress.serializers import PickleSerializer
from regress.storages import LocalDirectoryStorage


@pytest.fixture(scope='module')
def base_regress():
    regress = DefaultBaseRegress(
        storage=LocalDirectoryStorage('.regress/examples'),
        serializer=PickleSerializer(),
    )
    regress.storage.ensure_exists()
    yield regress

@pytest.fixture(scope='function')
def regress(base_regress, request):
    regress = Regress(base_regress, PytestContext(request))
    yield regress
