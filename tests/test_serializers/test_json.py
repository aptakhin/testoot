from io import BytesIO, TextIOWrapper

import pytest

from testoot.serializers import JsonSerializer


def test_simple():
    serializer = JsonSerializer()

    out = BytesIO()
    wrapper = TextIOWrapper(out)
    obj = {'a': 1}
    serializer.dump(obj, wrapper)
    wrapper.flush()
    out_bytes = out.getvalue()
    assert out_bytes == b'''{
  "a": 1
}'''

    in_ = TextIOWrapper(BytesIO(out_bytes))
    read_obj = serializer.load(in_)
    assert read_obj == obj


if __name__ == '__main__':
    pytest.main(['-s', __file__])
