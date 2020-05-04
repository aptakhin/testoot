# Regress

![](https://github.com/aptakhin/regress/workflows/Regress%20test/badge.svg)
[![codecov](https://codecov.io/gh/aptakhin/regress/branch/master/graph/badge.svg)](https://codecov.io/gh/aptakhin/regress)
[![Documentation Status](https://readthedocs.org/projects/regress/badge/?version=latest)](https://regress.readthedocs.io/en/latest/?badge=latest)
[![Maintainability](https://api.codeclimate.com/v1/badges/4bab5c99811799725609/maintainability)](https://codeclimate.com/github/aptakhin/regress/maintainability)

Regression testing framework for Python 3.4+. It's useful in unit and module testing when creating or rewriting test data is too boring. After you canonized the ideal output result all tests will pass until the data changes moment.

- Writes data to the local filesystem storage
- Supports binary, text, json and picklable objects
- Different policies for resolving test conflicts

Currently integrates best with the PyTest, but other frameworks are also welcomed.

## Example

One pytest function is the scope of the result. Newly calculated data compares with the original canonized result.

    # regress is the function scope helper fixture easy to setup
    def test_simple(regress: RegressFixture):
        result = {'a': 1}
        regress.test(result)  # Commit first time

        result2 = {'a': 1}
        regress.test(result2)  # Ok. No object result changes

        result3 = {'a': 3}  # Try commit change. Raised the AssertionError
        with pytest.raises(AssertionError) as e:
            regress.test(result3)

To continue exploring you can visit the [quickstart](https://regress.readthedocs.io/en/latest/usage/quickstart.html).

## Using

    pip3 install regress

## Documentation

https://regress.readthedocs.io/

## Development

Making virtualenv with development requirements:

    python3 -m venv venv
    venv/bin/pip install --upgrade pip
    venv/bin/pip install -r requirements.txt

## Testing

    venv/bin/pytest -s tests
    venv/bin/flake8 regress --show-source --statistics
    venv/bin/pytest --cov=regress --cov-report html
    
Or for automatizing:
    
    cp TEST.sh.example TEST.sh
    chmod +x TEST.sh
    ./TEST.sh

Some tests uses console for user interaction. Add `--canonize` flag:

    venv/bin/pytest -s tests --canonize

### Building docs

Using `sphinx`:

    cd docs
    make
