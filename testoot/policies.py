from testoot.base import TestootTestResult, CanonizePolicy, UserInteraction


class AskCanonizePolicy(CanonizePolicy):
    """If context allows to show canonization dialog then use provided
    user interaction."""
    def __init__(self, user_interaction: UserInteraction):
        self._user_interaction = user_interaction

    def ask_canonize(self, test_result: TestootTestResult) -> bool:
        answer = self._user_interaction.ask_canonize(test_result)
        return answer


class NoCanonizePolicy(CanonizePolicy):
    """Raises exception on any data mismatch in testing."""
    def ask_canonize(self, test_result: TestootTestResult) -> bool:
        return False
