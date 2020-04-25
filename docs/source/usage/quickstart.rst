Quickstart
===================================

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

    from regress.ext.pytest import PytestContext
    from regress.ext.simple import LocalRegress
    from regress.fixture import RegressFixture


    @pytest.fixture(scope='module')
    def regress_instance():
        regress = LocalRegress()
        regress.ensure_exists(clear=True)
        yield regress


    @pytest.fixture(scope='function')
    def regress(regress_instance, request):
        fixture = RegressFixture(regress_instance,
            PytestContext(request))
        yield fixture


LocalRegress is the configured class::

    from regress.impl.run_policy.no_canonize_policy import NoCanonizePolicy
    from regress.impl.serializer.pickle_serializer import PickleSerializer
    from regress.impl.storage.local_directory_storage import \
        LocalDirectoryStorage
    from regress.regress import Regress


    class LocalRegress(Regress):
        def __init__(self):
            super().__init__(
                storage=LocalDirectoryStorage('.regress'),
                serializer=PickleSerializer(),
                run_policy=NoCanonizePolicy(),
            )

It uses local filesystem storage in `.regress` directory.

All objects are dumped with pickle serializer, which is supports almost all Python objects, but has only binary representantion in files. It'll be difficult to merge binary changes in the favourite VCS without running code.

And third `run_policy` option shows running tests behaviour when we met result test conflict. :py:class:`.regress.impl.run_policy.no_canonize_policy.NoCanonizePolicy` raises an error in assert. :py:class:`.regress.impl.run_policy.ask_canonize_policy.AskCanonizePolicy` can ask user approval for canonizing new behaviour or skipping it later and raising an error in assert then. Latter can't be used in automated tests, but is useful in manual runs.
