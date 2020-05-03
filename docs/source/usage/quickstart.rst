Quickstart
===================================

You can install latest version from pypi::

    pip3 install regress

And use library such way.

Example::

    # regress is the helper fixture easy to setup
    def test_simple(regress: RegressFixture):
        result = {'a': 1}
        regress.test(result)  # Commit first time

        result2 = {'a': 1}
        regress.test(result2)  # Ok. No object result changes

        result3 = {'a': 3}  # Try commit change. Raised the AssertionError
        with pytest.raises(AssertionError) as e:
            regress.test(result3)


Pytest configuration is the quite simple::

    import pytest

    from regress.ext.pytest import PytestContext, register_addoption
    from regress.ext.simple import DefaultRegress
    from regress.fixture import RegressFixture

    def pytest_addoption(parser):
        register_addoption(parser)

    @pytest.fixture(scope='module')
    def regress_instance():
        regress = DefaultRegress()
        regress.ensure_exists(clear=True)
        yield regress

    @pytest.fixture(scope='function')
    def regress(regress_instance, request):
        fixture = RegressFixture(regress_instance,
            PytestContext(request))
        yield fixture


DefaultRegress is the configured class::

    from regress.pub import NoCanonizePolicy, PickleSerializer, \
        LocalDirectoryStorage, Regress

    class DefaultRegress(Regress):
        def __init__(self):
            super().__init__(
                storage=LocalDirectoryStorage('.regress'),
                serializer=PickleSerializer(),
                canonize_policy=AskCanonizePolicy(ConsoleUserInteraction())),
            )

It uses local filesystem storage in `.regress` directory in `storage` parameter.

All objects are dumped with pickle `serializer` :py:class:`.regress.pub.PickleSerializer`, which is supports almost all Python objects, but has only binary representantion in files. It'll be difficult to merge binary changes in the favourite VCS without running code. You can find other serializers in `Serializers <../api/serializer.html>`__ page.

Parameter `canonize_policy` controls behavior when we met result test conflict:

- :py:class:`.regress.pub.AskCanonizePolicy` (default) with `--canonize` pytest flag asks user approval for canonizing. If user refuses it skips for later and raises an error in assert then. For supporing `--canonize` flag :py:func:`.regress.ext.pytest.register_addoption` have to be called in `conftest.py`.

- :py:class:`.regress.pub.NoCanonizePolicy` always raises an error in assert.
