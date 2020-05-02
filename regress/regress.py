from typing import Optional

from regress.base import RegressStorage, RegressSerializer, \
    CanonizePolicy, RegressContext, FileType, Comparator


class Regress:
    """Main regression management object. Can test data."""

    def __init__(self, storage: RegressStorage, serializer: RegressSerializer,
                 canonize_policy: CanonizePolicy,
                 comparator: Optional[Comparator] = None):
        """Constructor

        :param storage: storage instance
        :param serializer: serializer instance
        :param canonize_policy: canonize policy instance
        :param comparator: base comparator
        """
        self._storage: RegressStorage = storage
        self._serializer: RegressSerializer = serializer
        self._canonize_policy: CanonizePolicy = canonize_policy
        self._comparator: Comparator = comparator

    def test(self, obj: any, context: RegressContext,
             suffix: Optional[str] = None,
             file_type_hint: Optional[FileType] = None,
             comparator: Optional[Comparator] = None):
        """Tests object

        :param obj: test object
        :param context: test context
        :param suffix: test suffix for making a few regression tests
               in one context
        :param file_type_hint: override serializer hint for file
        :param comparator: custom comparator override

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
                comparator=comparator,
                storage_name=storage_name,
                context=context,
            )

        return True

    def test_filename(self, filename: str, *, context: RegressContext,
                      comparator: Optional[Comparator] = None):
        """Tests filename generated by software

        :param filename: test filename
        :param context: test context
        :param comparator: custom comparator override

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
                comparator=comparator,
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

    def _do_test(self, *, test_obj: any, canon_obj: any,
                 storage_name: str, context: RegressContext,
                 comparator: Optional[Comparator] = None):
        comparator = self._get_comparator(context, comparator)

        if canon_obj is None:
            return self._canonize(test_obj, storage_name=storage_name)

        try:
            comparator.compare(test_obj, canon_obj)
        except Exception as e:
            do_canonize = self._canonize_policy.ask_canonize(
                context, exc=e,
            )
            if not do_canonize:
                raise

            return self._canonize(test_obj, storage_name=storage_name)

    def _get_comparator(self, context: RegressContext,
                        comparator: Optional[Comparator] = None) -> Comparator:
        if comparator is None:
            comparator = context.get_comparator()

            if comparator is None:
                comparator = self._comparator

            if comparator is None:
                raise RuntimeError('No comparator given in pipeline!')

        return comparator
