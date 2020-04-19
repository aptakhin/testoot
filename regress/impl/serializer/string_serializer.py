from regress.serializer import RegressSerializer


class StringSerializer(RegressSerializer):
    """Serializer only for string type (utf-8)"""
    def load(self, stream):
        return stream.read().decode("utf-8")

    def dump(self, obj, stream):
        return stream.write(obj.encode("utf-8"))
