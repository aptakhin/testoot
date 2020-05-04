from io import BytesIO

import pytest

from regress.pub import UnserializableTypeError
from regress.serializers import BinarySerializer


def test_simple():
    serializer = BinarySerializer()

    out = BytesIO()
    obj = b'abc'
    serializer.dump(obj, out)
    out_bytes = out.getvalue()
    assert out_bytes == b'abc'

    in_ = BytesIO(out_bytes)
    read_obj = serializer.load(in_)
    assert read_obj == obj


def test_only_binary():
    serializer = BinarySerializer()
    out = BytesIO()
    obj = {'a': 1}
    with pytest.raises(UnserializableTypeError):
        serializer.dump(obj, out)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
