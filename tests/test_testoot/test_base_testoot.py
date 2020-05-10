from testoot.base_testoot import BaseTestoot
from testoot.serializers import BinarySerializer, JsonSerializer
from tests.test_testoot.conftest import ContextTestoot, FalseComparator


def test_override_comparator(base_testoot: BaseTestoot):
    context = ContextTestoot('test-1')
    cmp1 = base_testoot._get_comparator(None, context=context)
    assert cmp1 == context.get_comparator()

    false_cmp = FalseComparator()
    cmp2 = base_testoot._get_comparator(false_cmp, context=context)
    assert cmp2 == false_cmp


def test_override_serializer(base_testoot: BaseTestoot):
    context = ContextTestoot('test-1')
    ser1 = base_testoot._get_serializer(None, context=context)
    assert ser1 == base_testoot._serializer

    json_serializer = JsonSerializer()
    context = ContextTestoot('test-1', serializer=json_serializer)
    ser2 = base_testoot._get_serializer(None, context=context)
    assert ser2 == json_serializer

    binary_serializer = BinarySerializer()
    ser3 = base_testoot._get_serializer(binary_serializer, context=context)
    assert ser3 == binary_serializer
