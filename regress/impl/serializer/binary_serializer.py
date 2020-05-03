from io import IOBase
from typing import Optional

from regress.exceptions import UnserializableTypeError
from regress.base import FileType, RegressSerializer


class BinarySerializer(RegressSerializer):
    """Serializer for binary data"""

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
