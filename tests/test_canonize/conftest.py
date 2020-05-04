import pytest

from regress.ext.pytest import PytestContext
from regress.pub import \
    AskCanonizePolicy, ConstantUserInteraction
from regress.regress import Regress
from regress.serializers import JsonSerializer


@pytest.fixture(scope='module')
def base_regress(root_base_regress):
    regress = root_base_regress.clone(
        storage=root_base_regress.storage.clone(add_path='canonize'),
        serializer=JsonSerializer(),
        canonize_policy=AskCanonizePolicy(
            ConstantUserInteraction(canonize=False),
        ),
    )
    regress.storage.ensure_exists()
    yield regress


class CanonizeRegress(Regress):
    def __init__(self, regress_base, context):
        super().__init__(regress_base, context)

    def set_canonize(self, canonize):
        self.canonize_policy._user_interaction.canonize = canonize


@pytest.fixture(scope='function')
def regress(base_regress, request):
    regress = CanonizeRegress(base_regress,
                              PytestContext(request, ask_canonize=True))
    yield regress
