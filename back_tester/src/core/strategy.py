from abc import ABC, abstractmethod


class AbstractStrategy(ABC):
    id: str

    @abstractmethod
    def isSell(self, index) -> bool:
        pass

    @abstractmethod
    def isBuy(self, index) -> bool:
        pass

    @abstractmethod
    def isStop(self, index, position) -> bool:
        pass


class EmptyStrategy_1(AbstractStrategy):
    id = "EmptyStrategy_1"

    def isSell(self, index):
        return True

    def isBuy(self, index) -> bool:
        return False

    def isStop(self, index, position) -> bool:
        return False

    def __repr__(self):
        return "Empty strategy 1"


class EmptyStrategy_2(AbstractStrategy):
    id = "EmptyStrategy_2"

    def isSell(self, index):
        return True

    def isBuy(self, index) -> bool:
        return False

    def isStop(self, index, position) -> bool:
        return False

    def __repr__(self):
        return "Empty strategy 2"
