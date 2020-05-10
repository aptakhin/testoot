Quickstart
===================================

You can install latest version from pypi::

    pip3 install testoot

And use library such way:

.. literalinclude:: ../../../tests/test_examples/test_quickstart.py
   :start-after: # region: test_simple
   :end-before: # endregion: test_simple

Pytest configuration is the quite simple:

.. literalinclude:: ../../../tests/test_examples/test_quickstart.py
   :start-after: # region: header
   :end-before: # endregion: header

Basically DefaultTestoot is the configured class::

    from testoot.pub import Testoot, AskCanonizePolicy, PickleSerializer, \
        LocalDirectoryStorage, DefaultTestoot, ConsoleUserInteraction

    class DefaultTestoot(Testoot):
        def __init__(self):
            super().__init__(
                storage=LocalDirectoryStorage('.regress'),
                serializer=PickleSerializer(),
                canonize_policy=AskCanonizePolicy(ConsoleUserInteraction())),
            )

It uses local filesystem storage in `.testoot` directory in `storage` parameter.

All objects are dumped with pickle `serializer` :py:class:`.testoot.pub.PickleSerializer`, which is supports almost all Python objects, but has only binary representantion in files. It'll be difficult to merge binary changes in the favourite VCS without running code. You can find other serializers in `Serializers <../api/serializers.html>`__ page.

Parameter `canonize_policy` controls behavior when we met result test conflict:

- :py:class:`.testoot.pub.AskCanonizePolicy` (default) with `--canonize` pytest flag asks user approval for canonizing. If user refuses it skips for later and raises an error in assert then. For supporing `--canonize` flag :py:func:`.testoot.ext.pytest.register_addoption` have to be called in `conftest.py`.

- :py:class:`.testoot.pub.NoCanonizePolicy` always raises an error in assert.
