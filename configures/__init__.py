import enum

from typing import ValuesView, TypeVar, AbstractSet

T = TypeVar("T", bound=enum.Enum)


class BaseEnumType(enum.Enum):
    @classmethod
    def member_names(cls) -> AbstractSet[str]:
        return cls.__members__.keys()

    @classmethod
    def member_values(cls) -> ValuesView[T]:
        return cls.__members__.values()

    @classmethod
    def to_doc(cls) -> str:
        return '；'.join([':'.join([str(ins.name), str(ins.value)]) for ins in cls])
