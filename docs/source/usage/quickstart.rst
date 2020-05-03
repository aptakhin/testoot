Quickstart
===================================

You can install latest version from pypi::

    pip3 install regress

And use library such way:

.. literalinclude:: ../../../tests/test_examples/test_quickstart.py
   :start-after: # region: test_simple
   :end-before: # endregion: test_simple

Pytest configuration is the quite simple:

.. literalinclude:: ../../../tests/test_examples/test_quickstart.py
   :start-after: # region: header
   :end-before: # endregion: header

Basically DefaultRegress is the configured class::

    from regress.pub import Regress, AskCanonizePolicy, PickleSerializer, \
        LocalDirectoryStorage, DefaultRegress, ConsoleUserInteraction

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
