Quickstart
===================================

Example::

    # regress is the helper fixture easy to setup
    def test_simple(regress: RegressFixture):
        result = {'a': 1}
        regress.test(result)  # Commit

        result2 = {'a': 1}
        regress.test(result2)  # Ok. No changes

        result3 = {'a': 3}  # Try commit change. Raised the AssertionError
        with pytest.raises(AssertionError) as e:
            regress.test(result3)



Configuration is quite simple::

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
