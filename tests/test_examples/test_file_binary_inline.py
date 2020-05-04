from pathlib import Path

from regress.fixture import RegressFixture
from regress.pub import BinarySerializer


def generate_file():
    filename = Path('.regress/console/generated_file_inline.txt')
    filename.write_bytes(b'abc')
    return filename


def test_file(binary_regress: RegressFixture):
    binary_regress.test_filename(generate_file(),
                                 serializer=BinarySerializer())
