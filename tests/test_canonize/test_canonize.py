from pathlib import Path

import pytest

from tests.test_canonize.conftest import CanonizeTestoot


def test_canonize_false(testoot: CanonizeTestoot):
    result = {'a': 1}
    testoot.test(result)  # Commit

    result2 = {'a': 1}
    testoot.test(result2)  # No changes

    testoot.set_canonize(False)
    result3 = {'a': 2}  # Try commit change
    with pytest.raises(AssertionError) as e:
        testoot.test(result3)

    result4 = {'a': 2}  # Try commit change again. No chance
    with pytest.raises(AssertionError) as e:
        testoot.test(result4)


def test_canonize_true(testoot: CanonizeTestoot):
    result = {'a': 1}
    testoot.test(result)  # Commit

    result2 = {'a': 1}
    testoot.test(result2)  # No changes

    testoot.set_canonize(True)
    result3 = {'a': 2}  # Try commit change and canonize
    testoot.test(result3)

    testoot.set_canonize(False)
    result4 = {'a': 2}  # Try commit already changed state
    testoot.test(result4)


def test_suffix(testoot: CanonizeTestoot):
    result = {'a': 1}
    testoot.test(result)

    result2 = {'a': 2}
    testoot.test(result2, suffix='_abc')  # Second test result


def test_filename(testoot: CanonizeTestoot):
    d = Path(testoot.storage.root_dir / 'hello.json')
    d.write_text('{}')

    testoot.test_filename(str(d))  # Canonize
    testoot.test_filename(str(d))  # Test


if __name__ == '__main__':
    pytest.main(['-s', __file__])
