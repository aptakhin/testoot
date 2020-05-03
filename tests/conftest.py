import pytest

from regress.ext.pytest import register_addoption


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


def pytest_runtest_setup(item):
    # Skip tests marked with console without --console option
    if any(mark for mark in item.iter_markers(name='console')):
        if not item.config.getoption('--console'):
            pytest.skip('test requires --console flag')
