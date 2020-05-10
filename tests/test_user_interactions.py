from unittest.mock import MagicMock

from testoot.user_interactions import ConsoleUserInteraction, \
    ConstantUserInteraction
from tests.conftest import AbcDiffResult


def test_console_parse():
    ui = ConsoleUserInteraction()

    assert ui.parse_input('Y')
    assert not ui.parse_input('nnn')
    assert not ui.parse_input('')


def test_console():
    test_result = AbcDiffResult()
    ui = ConsoleUserInteraction()
    ui.show_diff = MagicMock(return_value='')

    ui._ask_user_canonize = MagicMock(return_value='y')
    assert ui.ask_canonize(test_result)

    ui._ask_user_canonize = MagicMock(return_value='n')
    assert not ui.ask_canonize(test_result)


def test_constant():
    test_result = AbcDiffResult()

    true_ui = ConstantUserInteraction(canonize=True)
    assert true_ui.ask_canonize(test_result)

    false_ui = ConstantUserInteraction(canonize=False)
    assert not false_ui.ask_canonize(test_result)
