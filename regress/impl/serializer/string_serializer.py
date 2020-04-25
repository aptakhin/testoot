from typing import Optional

from regress.exceptions import UnserializableTypeError
from regress.file_type import FileType
from regress.serializer import RegressSerializer


class StringSerializer(RegressSerializer):
    """Serializer only for string type (utf-8)"""

    def __init__(self, file_type_hint: Optional[FileType] = None):
        super().__init__(file_type_hint=file_type_hint if file_type_hint else
                         FileType(mime='text/plain', override_file_ext='.txt'))

    def load(self, stream):
        return stream.read()

    def dump(self, obj, stream):
        if not isinstance(obj, str):
            raise UnserializableTypeError('Only str type is supported '
                                          'in StringSerializer!')
        return stream.write(obj)
