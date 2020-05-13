import enum


class BaseEnumType(enum.Enum):
    @classmethod
    def member_names(cls):
        return cls.__members__.keys()

    @classmethod
    def member_values(cls):
        return cls.__members__.values()

    @classmethod
    def to_doc(cls):
        return '；'.join([':'.join([str(ins.name), str(ins.value)]) for ins in cls])
