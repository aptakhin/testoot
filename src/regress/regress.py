import os
import pickle
from pathlib import Path
from typing import Optional

from src.regress.context import RegressContext
from src.regress.serializer import RegressSerializer
from src.regress.storage import RegressStorage


class Regress:
    def __init__(self, storage: RegressStorage, serializer: RegressSerializer):
        self._storage: RegressStorage = storage
        self._serializer: RegressSerializer = serializer

    def test(self, obj: any, context: RegressContext,
             suffix: Optional[str]=None):
        """Tests object

        :param obj: test object
        :param context: test context
        :param suffix: suffix for test for making a few regression tests in one
        context
        :return:
        """

        storage_name = context.get_storage_name(suffix=suffix)
        with self._storage.open_read(storage_name) as rstream:
            if rstream is not None:
                read_obj = self._serializer.load(rstream)
                assert obj == read_obj
            else:
                self.canonize(obj, context=context, suffix=suffix)

        return True

    def canonize(self, obj: any, context: RegressContext,
             suffix: Optional[str]=None):
        """Canonizes results of tests

        :param obj: test object
        :param context: test context
        :param suffix: suffix for test for making a few regression tests in one
        :return:
        """
        storage_name = context.get_storage_name(suffix=suffix)
        with self._storage.open_write(storage_name) as wstream:
            self._serializer.dump(obj, wstream)
