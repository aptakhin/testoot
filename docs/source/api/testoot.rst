Testoot
===================================

Testoot is the main logic class for testing. It's configured by storage, serializer and canonize policy.

.. autoclass:: testoot.pub.BaseTestoot
  :members:

.. autoclass:: testoot.pub.Testoot
  :members:

Context stores current test information.

.. autoclass:: testoot.base.TestootContext
  :members:

.. autoclass:: testoot.base.TestootTestResult
  :members:

.. autoclass:: testoot.base.Comparator
  :members:


FileType is the hint from the serializer to which file type result can be saved for simplifying viewing and merging results.

.. autoclass:: testoot.base.FileType
  :members:

Exceptions

.. automodule:: testoot.exceptions
  :members:
