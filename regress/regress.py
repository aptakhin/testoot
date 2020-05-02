from typing import Optional

from regress.base import Comparator, RegressStorage, RegressSerializer, \
    CanonizePolicy, RegressContext, FileType


class Regress:
    """Main regression management object. Can test data."""

    def __init__(self, storage: RegressStorage, serializer: RegressSerializer,
                 canonize_policy: CanonizePolicy):
        """Constructor

        :param storage: storage instance
        :param serializer: serializer instance
        :param canonize_policy: canonize policy instance
        """
        self._storage: RegressStorage = storage
        self._serializer: RegressSerializer = serializer
        self._canonize_policy: CanonizePolicy = canonize_policy
        self._comparator: Comparator = None

    def test(self, obj: any, context: RegressContext,
             suffix: Optional[str] = None,
             file_type_hint: Optional[FileType] = None):
        """Tests object

        :param obj: test object
        :param context: test context
        :param suffix: suffix for test for making a few regression tests
               in one context
        :param file_type_hint: override serializer hint for file

        :return:
        """
        if file_type_hint is None:
            file_type_hint = self._serializer.file_type_hint

        storage_name = context.get_storage_name(suffix=suffix,
                                                file_type_hint=file_type_hint)
        with self._storage.open_read(storage_name) as rstream:
            canon_obj = (self._serializer.load(rstream) if rstream is not None
                         else None)

            self._do_test(
                test_obj=obj,
                canon_obj=canon_obj,
                comparator=self._comparator,
                storage_name=storage_name,
                context=context,
            )

        return True

    def test_filename(self, filename: str, *, context: RegressContext):
        """Tests object

        :param filename: test filename
        :param context: test context

        :return:
        """

        storage_name = context.get_storage_name_from_filename(filename)
        with self._storage.open_read(storage_name) as rstream:
            canon_obj = (self._serializer.load(rstream) if rstream is not None
                         else None)

            with self._storage.open_read(filename) as test_stream:
                test_obj = self._serializer.load(test_stream)

                self._do_test(
                    test_obj=test_obj,
                    canon_obj=canon_obj,
                    comparator=self._comparator,
                    storage_name=storage_name,
                    context=context,
                )

        return True

    def _canonize(self, obj: any, *, storage_name: str):
        """Canonizes result of test

        :param obj: test object
        :param storage_name: storage name

        :return:
        """
        with self._storage.open_write(storage_name) as wstream:
            self._serializer.dump(obj, wstream)

    def _do_test(self, *, test_obj: any, canon_obj: any, comparator,
                 storage_name: str, context: RegressContext):
        if canon_obj is None:
            return self._canonize(test_obj, storage_name=storage_name)

        try:
            assert test_obj == canon_obj
        except Exception as e:
            do_canonize = self._canonize_policy.ask_canonize(
                context, exc=e,
            )
            if not do_canonize:
                raise

            return self._canonize(test_obj, storage_name=storage_name)
