from regress.base import RegressTestResult, UserInteraction


class ConsoleUserInteraction(UserInteraction):
    def ask_canonize(self, test_result: RegressTestResult) -> bool:
        diff = test_result.format_diff()
        print(diff)
        answer = input("Canonize [yn]? ")  # pragma: no cover
        return answer.lower() in ('y',)  # pragma: no cover


class ConstantUserInteraction(UserInteraction):
    def __init__(self, *, canonize):
        self.canonize = canonize

    def ask_canonize(self, test_result: RegressTestResult) -> bool:
        return self.canonize
