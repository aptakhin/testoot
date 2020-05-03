from pathlib import Path

import pytest

from regress.ext.pytest import PytestContext
from regress.fixture import RegressFixture
from regress.pub import BinarySerializer


@pytest.fixture(scope='function')
def binary_regress(regress_instance, request):
    fixture = RegressFixture(regress_instance, PytestContext(request,
                             serializer=BinarySerializer()))
    yield fixture


def generate_file():
    filename = Path('.regress/console/generated_file.txt')
    filename.write_bytes(b'abc')
    return filename


def test_file(binary_regress: RegressFixture):
    binary_regress.test_filename(generate_file())
