import pickle
from typing import Optional

from regress.file_type import FileType
from regress.serializer import RegressSerializer


class PickleSerializer(RegressSerializer):
    """Good serializer for almost all Python objects. But binary"""
    PICKLE_PROTOCOL_VERSION = 4

    def __init__(self, file_type_hint: Optional[FileType] = None):
        super().__init__(file_type_hint=file_type_hint if file_type_hint else
                         FileType(mime='application/octet-stream',
                                  override_file_ext='.bin'))

    def load(self, stream):
        return pickle.load(stream)

    def dump(self, obj, stream):
        return pickle.dump(obj, stream, protocol=self.PICKLE_PROTOCOL_VERSION)
