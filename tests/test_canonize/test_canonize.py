from pathlib import Path

import pytest

from tests.test_canonize.conftest import CanonizeRegress


def test_canonize_false(regress: CanonizeRegress):
    result = {'a': 1}
    regress.test(result)  # Commit

    result2 = {'a': 1}
    regress.test(result2)  # No changes

    regress.set_canonize(False)
    result3 = {'a': 2}  # Try commit change
    with pytest.raises(AssertionError) as e:
        regress.test(result3)

    result4 = {'a': 2}  # Try commit change again. No chance
    with pytest.raises(AssertionError) as e:
        regress.test(result4)


def test_canonize_true(regress: CanonizeRegress):
    result = {'a': 1}
    regress.test(result)  # Commit

    result2 = {'a': 1}
    regress.test(result2)  # No changes

    regress.set_canonize(True)
    result3 = {'a': 2}  # Try commit change and canonize
    regress.test(result3)

    regress.set_canonize(False)
    result4 = {'a': 2}  # Try commit already changed state
    regress.test(result4)


def test_suffix(regress: CanonizeRegress):
    result = {'a': 1}
    regress.test(result)

    result2 = {'a': 2}
    regress.test(result2, suffix='_abc')  # Second test result


def test_filename(regress: CanonizeRegress):
    d = Path(regress.storage.root_dir / 'hello.json')
    d.write_text('{}')

    regress.test_filename(str(d))  # Canonize
    regress.test_filename(str(d))  # Test


if __name__ == '__main__':
    pytest.main(['-s', __file__])
