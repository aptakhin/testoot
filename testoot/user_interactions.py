from testoot.base import TestootTestResult, UserInteraction


class ConsoleUserInteraction(UserInteraction):
    """Interactive console canonization asker."""
    def ask_canonize(self, test_result: TestootTestResult) -> bool:
        """Prints diff and asks user to canonize diff. If get `y`
        returns True."""
        diff = test_result.format_diff()
        self.show_diff(diff)
        answer = self._ask_user_canonize()
        return self.parse_input(answer)

    @staticmethod
    def show_diff(diff: str):
        print(diff)

    @staticmethod
    def parse_input(value: str) -> bool:
        return value.lower() in ('y',)

    @staticmethod
    def _ask_user_canonize() -> str:
        return input("Canonize [yn]? ")  # pragma: no cover


class ConstantUserInteraction(UserInteraction):
    """Have constant response to all canonize requests."""
    def __init__(self, *, canonize):
        self.canonize = canonize

    def ask_canonize(self, test_result: TestootTestResult) -> bool:
        """Returns stored `canonize` value."""
        return self.canonize
