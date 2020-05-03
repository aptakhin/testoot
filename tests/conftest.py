import pytest

from regress.ext.pytest import register_addoption, \
    PytestContext
from regress.fixture import RegressFixture
from regress.pub import AskCanonizePolicy, PickleSerializer, \
    LocalDirectoryStorage, ConsoleUserInteraction, BinarySerializer
from regress.regress import Regress


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    register_addoption(parser)
    parser.addoption(
        '--console',
        action='store_true',
        help='run tests using user console input.',
    )


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line(
        'markers', 'console(name): mark test to run only with --console'
    )
    config.addinivalue_line(
        'markers', 'no_console(name): mark test not to run only with --console'
    )


def pytest_runtest_setup(item):
    # Skip tests marked with console without --console option
    if any(mark for mark in item.iter_markers(name='console')):
        if not item.config.getoption('--console'):
            pytest.skip('test requires --console flag')

    # Skip tests marked with no_console with --console option
    if any(mark for mark in item.iter_markers(name='no_console')):
        if item.config.getoption('--console'):
            pytest.skip('test no --console flag')


class TestRegress(Regress):
    """Test regress"""
    def __init__(self):
        super().__init__(
            storage=LocalDirectoryStorage('.regress/console'),
            serializer=PickleSerializer(),
            canonize_policy=AskCanonizePolicy(ConsoleUserInteraction()),
        )

    def ensure_exists(self, clear=False):
        return self._storage.ensure_exists(clear=clear)


@pytest.fixture(scope='module')
def regress_instance():
    regress = TestRegress()
    regress.ensure_exists(clear=True)
    yield regress


@pytest.fixture(scope='function')
def regress(regress_instance, request):
    fixture = RegressFixture(regress_instance, PytestContext(request))
    yield fixture


@pytest.fixture(scope='function')
def binary_regress(regress_instance, request):
    fixture = RegressFixture(regress_instance, PytestContext(request,
                             serializer=BinarySerializer()))
    yield fixture
