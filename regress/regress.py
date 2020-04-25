from typing import Optional

from regress.context import RegressContext
from regress.file_type import FileType
from regress.run_policy import RunPolicy
from regress.serializer import RegressSerializer
from regress.storage import RegressStorage


class Regress:
    """
    Main regression management object. Can test and canonize data.
    """

    def __init__(self, storage: RegressStorage, serializer: RegressSerializer,
                 run_policy: RunPolicy):
        self._storage: RegressStorage = storage
        self._serializer: RegressSerializer = serializer
        self._run_policy: RunPolicy = run_policy

    def test(self, obj: any, context: RegressContext,
             suffix: Optional[str] = None,
             file_type_hint: Optional[FileType] = None):
        """Tests object

        :param obj: test object
        :param context: test context
        :param suffix: suffix for test for making a few regression tests in one
        context
        :param file_type_hint: override serializer hint for file
        :return:
        """
        if file_type_hint is None:
            file_type_hint = self._serializer.file_type_hint

        storage_name = context.get_storage_name(suffix=suffix,
                                                file_type_hint=file_type_hint)
        with self._storage.open_read(storage_name) as rstream:
            if rstream is not None:
                read_obj = self._serializer.load(rstream)
                try:
                    assert obj == read_obj
                except Exception as e:
                    do_canonize = self._run_policy.ask_canonize(
                        context, exc=e,
                    )
                    if do_canonize:
                        self.canonize(obj, context=context, suffix=suffix,
                                      file_type_hint=file_type_hint)
                    else:
                        raise
            else:
                self.canonize(obj, context=context, suffix=suffix,
                              file_type_hint=file_type_hint)

        return True

    def canonize(self, obj: any, context: RegressContext,
                 suffix: Optional[str] = None,
                 file_type_hint: Optional[FileType] = None):
        """Canonizes results of tests

        :param obj: test object
        :param context: test context
        :param suffix: suffix for test for making a few regression tests in one
        :param file_type_hint: override serializer hint for file
        :return:
        """
        storage_name = context.get_storage_name(suffix=suffix,
                                                file_type_hint=file_type_hint)
        with self._storage.open_write(storage_name) as wstream:
            self._serializer.dump(obj, wstream)
