from regress.context import RegressContext
from regress.run_policy import RunPolicy
from regress.user_interaction import UserInteraction


class AskCanonizePolicy(RunPolicy):
    def __init__(self, user_interaction: UserInteraction):
        self._user_interaction = user_interaction

    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        answer = self._user_interaction.ask_canonize(context=context, exc=exc)
        return answer
