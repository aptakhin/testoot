import mimetypes
from dataclasses import dataclass
from typing import Optional


class FileTypeNoExtension:
    pass


@dataclass
class FileType:
    """File type hint for tests.

    :param mime: required MIME type
    :param override_file_ext: override default MIME type extension
    """
    mime: str
    override_file_ext: Optional[str] = FileTypeNoExtension

    def get_file_extension(self) -> Optional[str]:
        if self.override_file_ext is not FileTypeNoExtension:
            return self.override_file_ext

        return mimetypes.guess_extension(self.mime, strict=False)
