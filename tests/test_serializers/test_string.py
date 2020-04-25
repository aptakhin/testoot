from io import StringIO

import pytest

from regress.exceptions import UnserializableTypeError
from regress.impl.serializer.string_serializer import StringSerializer


def test_simple():
    serializer = StringSerializer()

    out = StringIO()
    obj = 'abc'
    serializer.dump(obj, out)
    out_bytes = out.getvalue()
    assert out_bytes == '''abc'''

    in_ = StringIO(out_bytes)
    read_obj = serializer.load(in_)
    assert read_obj == obj


def test_only_string():
    serializer = StringSerializer()

    out = StringIO()
    obj = {'a': 1}
    with pytest.raises(UnserializableTypeError):
        serializer.dump(obj, out)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
