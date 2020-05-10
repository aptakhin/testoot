from pathlib import Path

import pytest

from testoot.ext.pytest import PytestContext
from testoot.testoot import Testoot
from testoot.serializers import BinarySerializer


@pytest.fixture(scope='function')
def binary_testoot(base_testoot, request):
    testoot = Testoot(base_testoot,
                      PytestContext(request, serializer=BinarySerializer()))
    yield testoot


def generate_file():
    filename = Path('.testoot/examples/generated_file.txt')
    filename.write_bytes(b'abc')
    return filename


def test_file(binary_testoot: Testoot):
    binary_testoot.test_filename(generate_file())
