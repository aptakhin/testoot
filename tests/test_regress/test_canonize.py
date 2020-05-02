import pytest

from regress.fixture import RegressFixture


def test_canonize_false(test_regress: RegressFixture):
    result = {'a': 1}
    test_regress.test(result)  # Commit

    result2 = {'a': 1}
    test_regress.test(result2)  # No changes

    test_regress._regress._canonize_policy._user_interaction.canonize = False
    result3 = {'a': 2}  # Try commit change
    with pytest.raises(AssertionError) as e:
        test_regress.test(result3)

    result4 = {'a': 2}  # Try commit change again. No chance
    with pytest.raises(AssertionError) as e:
        test_regress.test(result4)


def test_canonize_true(test_regress: RegressFixture):
    result = {'a': 1}
    test_regress.test(result)  # Commit

    result2 = {'a': 1}
    test_regress.test(result2)  # No changes

    test_regress._regress._canonize_policy._user_interaction.canonize = True
    result3 = {'a': 2}  # Try commit change and canonize
    test_regress.test(result3)

    test_regress._regress._canonize_policy._user_interaction.canonize = False
    result4 = {'a': 2}  # Try commit already changed state
    test_regress.test(result4)


def test_suffix(test_regress: RegressFixture):
    result = {'a': 1}
    test_regress.test(result)

    result2 = {'a': 2}
    test_regress.test(result2, suffix='_abc')  # Second test result


def test_filename(test_regress: RegressFixture, tmp_path):
    d = tmp_path / 'hello.json'
    d.write_text('{}')

    test_regress.test_filename(str(d))  # Canonize
    test_regress.test_filename(str(d))  # Test


if __name__ == '__main__':
    pytest.main(['-s', __file__])
