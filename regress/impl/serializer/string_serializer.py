from io import IOBase
from typing import Optional

from regress.exceptions import UnserializableTypeError
from regress.base import FileType, RegressSerializer


class StringSerializer(RegressSerializer):
    """Serializer only for string type (utf-8)"""

    def __init__(self, file_type_hint: Optional[FileType] = None):
        super().__init__(file_type_hint=file_type_hint if file_type_hint else
                         FileType(mime='text/plain', override_file_ext='.txt'))

    def load(self, stream: IOBase) -> any:
        return stream.read()

    def dump(self, obj: any, stream: IOBase):
        if not isinstance(obj, str):
            raise UnserializableTypeError('Only str type is supported '
                                          'in StringSerializer!')
        return stream.write(obj)
