import pickle

from src.regress.serializer import RegressSerializer


class PickleSerializer(RegressSerializer):
    PICKLE_PROTOCOL_VERSION = 4

    def load(self, stream):
        return pickle.load(stream)

    def dump(self, obj, stream):
        return pickle.dump(obj, stream, protocol=self.PICKLE_PROTOCOL_VERSION)
