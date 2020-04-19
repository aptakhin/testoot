# Regress

![](https://github.com/aptakhin/regress/workflows/Regress%20test/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/regress/badge/?version=latest)](https://regress.readthedocs.io/en/latest/?badge=latest)


Early draft for regression testing framework in Python 3.4+. Currently integrates best with the PyTest, but other frameworks are also welcomed. Regression testing is useful in unit and module testing when rewriting test data creating is too boring. After you canonized the ideal output result all tests will pass until the data changes moment.

## Example

    # regress is the function scope helper fixture easy to setup
    def test_simple(regress: RegressFixture):
        result = {'a': 1}
        regress.test(result)  # Commit

        result2 = {'a': 1}
        regress.test(result2)  # Ok. No changes

        result3 = {'a': 3}  # Try commit change. Raised the AssertionError
        with pytest.raises(AssertionError) as e:
            regress.test(result3)

## Using

    pip3 install regress

## Development

    python3 -m venv venv
    venv/bin/pip install --upgrade pip
    venv/bin/pip install -r requirements.txt

## Further plans

- Text Python object serialization for more transparent changes merging
- Canonization tool with merging tests renames
- Remote canonization data storages for not storing data in the repository
- Support for other Python test frameworks
