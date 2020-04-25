from regress.context import RegressContext
from regress.run_policy import RunPolicy


class NoCanonizePolicy(RunPolicy):
    def ask_canonize(self, context: RegressContext, exc: Exception) -> bool:
        return False
