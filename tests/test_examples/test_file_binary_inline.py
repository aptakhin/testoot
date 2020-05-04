from pathlib import Path

from regress.regress import Regress
from regress.serializers import BinarySerializer


def generate_file(root_dir):
    filename = Path(root_dir / 'generated_file_inline.txt')
    filename.write_bytes(b'abc')
    return filename


def test_file(regress: Regress):
    regress.test_filename(generate_file(regress.storage.root_dir),
                          serializer=BinarySerializer())
