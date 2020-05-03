from regress.base import RegressTestResult, CanonizePolicy, UserInteraction


class AskCanonizePolicy(CanonizePolicy):
    """"""
    def __init__(self, user_interaction: UserInteraction):
        self._user_interaction = user_interaction

    def ask_canonize(self, test_result: RegressTestResult) -> bool:
        answer = self._user_interaction.ask_canonize(test_result)
        return answer


class NoCanonizePolicy(CanonizePolicy):
    def ask_canonize(self, test_result: RegressTestResult) -> bool:
        return False
