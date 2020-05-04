import pytest

from regress.ext.simple import DefaultRegress


@pytest.fixture(scope='module')
def init_regress_instance():
    regress = DefaultRegress()
    regress.ensure_exists(clear=True)
    yield regress
