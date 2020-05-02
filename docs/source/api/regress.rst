Regress
===================================

Regress is the main logic class for testing. It's configured by storage, serializer and canonize policy.

.. autoclass:: regress.pub.Regress
  :members:

Fixture is the helper class which incapsulates current Regress and test context state

.. automodule:: regress.fixture
  :members:

Context stores current test information.

.. autoclass:: regress.base.RegressContext
  :members:

FileType is the hint from the serializer to which file type result can be saved for simplifying viewing and merging results.

.. autoclass:: regress.base.FileType
  :members:

Exceptions

.. automodule:: regress.exceptions
  :members:
