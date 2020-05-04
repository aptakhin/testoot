Policies
===================================

.. autoclass:: regress.base.CanonizePolicy
  :members:

.. autoclass:: regress.policies.AskCanonizePolicy
  :members:

.. autoclass:: regress.policies.NoCanonizePolicy
  :members:

.. autoclass:: regress.base.UserInteraction
  :members:

.. autoclass:: regress.user_interactions.ConstantUserInteraction
  :members:

.. autoclass:: regress.user_interactions.ConsoleUserInteraction
  :members:

Enabled console interaction with `--canonize` flag prints such text in console::

    tests/test_console/test_console.py [tests/test_console/test_console.py::test_simple]
    {'a': 2} == {'a': 1}
    ~Differing items:
    ~{'a': 2} != {'a': 1}
    ~Use -v to get the full diff
    Canonize [yn]? y
    .
