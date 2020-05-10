from io import BytesIO, TextIOWrapper

import pytest

from testoot.pub import UnserializableTypeError
from testoot.serializers import StringSerializer


def test_simple():
    serializer = StringSerializer()

    out = BytesIO()
    obj = 'abc'
    serializer.dump(obj, out)
    out_bytes = out.getvalue()
    assert out_bytes == b'abc'

    in_ = BytesIO(out_bytes)
    read_obj = serializer.load(in_)
    assert read_obj == obj


def test_only_string():
    serializer = StringSerializer()
    out = BytesIO()
    obj = {'a': 1}
    with pytest.raises(UnserializableTypeError):
        serializer.dump(obj, out)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
