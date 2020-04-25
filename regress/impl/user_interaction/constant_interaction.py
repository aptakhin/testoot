from regress.context import RegressContext
from regress.user_interaction import UserInteraction


class ConstantUserInteraction(UserInteraction):
    def __init__(self, *, canonize):
        self.canonize = canonize

    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        return self.canonize
