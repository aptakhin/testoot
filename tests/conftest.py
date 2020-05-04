import pytest

from regress.ext.pytest import register_addoption, \
    PytestContext
from regress.ext.simple import DefaultBaseRegress
from regress.pub import AskCanonizePolicy, LocalDirectoryStorage, \
    ConsoleUserInteraction
from regress.regress import Regress
from regress.serializers import BinarySerializer, PickleSerializer


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
        'markers', 'canonize(name): mark test to run only with --canonize'
    )
    config.addinivalue_line(
        'markers', 'no_canonize(name): mark test not to run only with '
        '--canonize'
    )


def pytest_runtest_setup(item):
    # Skip tests marked with console without --console option
    if any(mark for mark in item.iter_markers(name='canonize')):
        if not item.config.getoption('--canonize'):
            pytest.skip('test requires --canonize flag')

    # Skip tests marked with no_console with --console option
    if any(mark for mark in item.iter_markers(name='no_canonize')):
        if item.config.getoption('--canonize'):
            pytest.skip('test no --canonize flag')


@pytest.fixture(scope='module')
def root_base_regress():
    regress = DefaultBaseRegress(
        storage=LocalDirectoryStorage('.regress'),
        serializer=PickleSerializer(),
        canonize_policy=AskCanonizePolicy(ConsoleUserInteraction()),
    )
    regress.storage.clear_if_exists()
    regress.storage.ensure_exists()
    yield regress


@pytest.fixture(scope='function')
def root_regress(root_base_regress, request):
    fixture = Regress(root_base_regress, PytestContext(request))
    yield fixture


# @pytest.fixture(scope='function')
# def binary_regress(regress_instance, request):
#     fixture = Regress(regress_instance,
#                       PytestContext(request, serializer=BinarySerializer()))
#     yield fixture
