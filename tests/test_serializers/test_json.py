from io import StringIO

import pytest

from regress.pub import JsonSerializer


def test_simple():
    serializer = JsonSerializer()

    out = StringIO()
    obj = {'a': 1}
    serializer.dump(obj, out)
    out_bytes = out.getvalue()
    assert out_bytes == '''{
  "a": 1
}'''

    in_ = StringIO(out_bytes)
    read_obj = serializer.load(in_)
    assert read_obj == obj


if __name__ == '__main__':
    pytest.main(['-s', __file__])
