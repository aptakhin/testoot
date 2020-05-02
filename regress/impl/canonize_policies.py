from regress.base import RegressContext, CanonizePolicy, UserInteraction


class AskCanonizePolicy(CanonizePolicy):
    def __init__(self, user_interaction: UserInteraction):
        self._user_interaction = user_interaction

    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        answer = self._user_interaction.ask_canonize(context=context, exc=exc)
        return answer


class NoCanonizePolicy(CanonizePolicy):
    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        return False
