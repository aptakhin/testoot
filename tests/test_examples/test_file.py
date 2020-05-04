from pathlib import Path

import pytest

from regress.ext.pytest import PytestContext
from regress.regress import Regress
from regress.serializers import BinarySerializer


@pytest.fixture(scope='function')
def binary_regress(base_regress, request):
    regress = Regress(base_regress,
                      PytestContext(request, serializer=BinarySerializer()))
    yield regress


def generate_file():
    filename = Path('.regress/examples/generated_file.txt')
    filename.write_bytes(b'abc')
    return filename


def test_file(binary_regress: Regress):
    binary_regress.test_filename(generate_file())
