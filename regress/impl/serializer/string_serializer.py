import pickle

from regress.serializer import RegressSerializer


class PickleSerializer(RegressSerializer):
    """Good serializer for almost all Python objects. But binary"""
    PICKLE_PROTOCOL_VERSION = 4

    def load(self, stream):
        return pickle.load(stream)

    def dump(self, obj, stream):
        return pickle.dump(obj, stream, protocol=self.PICKLE_PROTOCOL_VERSION)
