Pytest
===================================

Primary testing framework implementation.
The most useful is class PytestContext, which compounds with :py:class:`.regress.pub.BaseRegress` for :py:class:`.regress.pub.Regress` initialization.

.. autoclass:: regress.ext.pytest.PytestContext
  :members:

.. automethod:: regress.ext.pytest.register_addoption

.. autoclass:: regress.ext.pytest.PytestComparator
  :members:

.. autoclass:: regress.ext.pytest.PytestResult
  :members:
