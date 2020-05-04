from pathlib import Path

from regress.regress import Regress
from regress.serializers import BinarySerializer


def generate_file():
    filename = Path('.regress/examples/generated_file_inline.txt')
    filename.write_bytes(b'abc')
    return filename


def test_file(regress: Regress):
    regress.test_filename(generate_file(),
                          serializer=BinarySerializer())
