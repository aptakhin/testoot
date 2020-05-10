from pathlib import Path

from testoot.testoot import Testoot
from testoot.serializers import BinarySerializer


def generate_file(root_dir):
    filename = Path(root_dir / 'generated_file_inline.txt')
    filename.write_bytes(b'abc')
    return filename


def test_file(testoot: Testoot):
    testoot.test_filename(generate_file(testoot.storage.root_dir),
                          serializer=BinarySerializer())
