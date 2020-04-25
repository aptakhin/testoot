from regress.context import RegressContext
from regress.user_interaction import UserInteraction


class ConsoleUserInteraction(UserInteraction):
    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        answer = input("Canonize?")
        return answer in ('y',)
