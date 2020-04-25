import json
from typing import Optional

from regress.filetype import FileType
from regress.serializer import RegressSerializer


class JsonSerializer(RegressSerializer):
    """Serializer only json data"""

    def __init__(self, file_type_hint: Optional[FileType] = None):
        super().__init__(file_type_hint=file_type_hint if file_type_hint else
                         FileType(mime='application/json'))

    def load(self, stream):
        return json.load(stream)

    def dump(self, obj, stream):
        return json.dump(obj, stream, indent=2, ensure_ascii=False)
