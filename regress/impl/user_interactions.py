from regress.base import RegressContext, UserInteraction


class ConsoleUserInteraction(UserInteraction):
    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        answer = input("Canonize?")  # pragma: no cover
        return answer in ('y',)  # pragma: no cover


class ConstantUserInteraction(UserInteraction):
    def __init__(self, *, canonize):
        self.canonize = canonize

    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        return self.canonize
