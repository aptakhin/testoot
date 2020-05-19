import pytest

from testoot.base import TestootTestResult
from testoot.ext.pytest import register_addoption, \
    PytestContext
from testoot.ext.simple import DefaultBaseTestoot
from testoot.pub import AskCanonizePolicy, LocalDirectoryStorage, \
    ConsoleUserInteraction
from testoot.testoot import Testoot
from testoot.serializers import BinarySerializer, PickleSerializer


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


def pytest_addoption(parser):
    register_addoption(parser)


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
    # Skip tests marked with canonize without --canonize option
    if any(mark for mark in item.iter_markers(name='canonize')):
        if not item.config.getoption('--canonize'):
            pytest.skip('test requires --canonize flag')

    # Skip tests marked with no_canonize with --canonize option
    if any(mark for mark in item.iter_markers(name='no_canonize')):
        if item.config.getoption('--canonize'):
            pytest.skip('test no --canonize flag')


@pytest.fixture(scope='module')
def root_base_testoot():
    regress = DefaultBaseTestoot(
        storage=LocalDirectoryStorage('.testoot'),
        serializer=PickleSerializer(),
        canonize_policy=AskCanonizePolicy(ConsoleUserInteraction()),
    )
    regress.storage.clear_if_exists()
    regress.storage.ensure_exists()
    yield regress


@pytest.fixture(scope='function')
def root_testoot(root_base_testoot, request):
    fixture = Testoot(root_base_testoot, PytestContext(request))
    yield fixture


class AbcDiffResult(TestootTestResult):
    def format_diff(self) -> str:
        return 'abc'
