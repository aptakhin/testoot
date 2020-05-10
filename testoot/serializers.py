import json
import pickle
from io import IOBase
from typing import Optional

from testoot.base import TestootSerializer, FileType
from testoot.exceptions import UnserializableTypeError


class BinarySerializer(TestootSerializer):
    """Serializer for binary data."""

    def __init__(self, file_type_hint: Optional[FileType] = None):
        super().__init__(file_type_hint=file_type_hint if file_type_hint else
                         FileType(mime='application/octet-stream',
                                  override_file_ext='.bin'))

    def load(self, stream: IOBase) -> any:
        return stream.read()

    def dump(self, obj: any, stream: IOBase):
        if not isinstance(obj, bytes):
            raise UnserializableTypeError('Only bytes type is supported '
                                          'in BinarySerializer!')
        return stream.write(obj)


class JsonSerializer(TestootSerializer):
    """Serializer for only json data."""

    def __init__(self, file_type_hint: Optional[FileType] = None):
        super().__init__(mode='t',
                         file_type_hint=file_type_hint if file_type_hint else
                         FileType(mime='application/json'))

    def load(self, stream: IOBase) -> any:
        return json.load(stream)

    def dump(self, obj: any, stream: IOBase):
        json.dump(obj, stream, indent=2, ensure_ascii=False)


class StringSerializer(TestootSerializer):
    """Serializer only for string type (utf-8)."""

    def __init__(self, file_type_hint: Optional[FileType] = None):
        super().__init__(file_type_hint=file_type_hint if file_type_hint else
                         FileType(mime='text/plain', override_file_ext='.txt'))

    def load(self, stream: IOBase) -> any:
        return stream.read().decode('utf-8')

    def dump(self, obj: any, stream: IOBase):
        if not isinstance(obj, str):
            raise UnserializableTypeError('Only str type is supported '
                                          'in StringSerializer!')
        return stream.write(obj.encode('utf-8'))


class PickleSerializer(TestootSerializer):
    """Binary serializer for almost all Python objects."""
    PICKLE_PROTOCOL_VERSION = 4

    def __init__(self, file_type_hint: Optional[FileType] = None):
        super().__init__(file_type_hint=file_type_hint if file_type_hint else
                         FileType(mime='application/octet-stream',
                                  override_file_ext='.bin'))

    def load(self, stream: IOBase) -> any:
        return pickle.load(stream)

    def dump(self, obj: any, stream: IOBase):
        return pickle.dump(obj, stream, protocol=self.PICKLE_PROTOCOL_VERSION)
