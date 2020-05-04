from regress.base_regress import BaseRegress
from regress.serializers import BinarySerializer, JsonSerializer
from tests.test_regress.conftest import ContextRegress, FalseComparator


def test_override_comparator(base_regress: BaseRegress):
    context = ContextRegress('test-1')
    cmp1 = base_regress._get_comparator(None, context=context)
    assert cmp1 == context.get_comparator()

    false_cmp = FalseComparator()
    cmp2 = base_regress._get_comparator(false_cmp, context=context)
    assert cmp2 == false_cmp


def test_override_serializer(base_regress: BaseRegress):
    context = ContextRegress('test-1')
    ser1 = base_regress._get_serializer(None, context=context)
    assert ser1 == base_regress._serializer

    json_serializer = JsonSerializer()
    context = ContextRegress('test-1', serializer=json_serializer)
    ser2 = base_regress._get_serializer(None, context=context)
    assert ser2 == json_serializer

    binary_serializer = BinarySerializer()
    ser3 = base_regress._get_serializer(binary_serializer, context=context)
    assert ser3 == binary_serializer
