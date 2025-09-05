from abc import ABC, abstractmethod


class Trader(ABC):
    @abstractmethod
    def run_session() -> float:
        pass


class SimpleTrader(Trader):
    def run_session(self) -> float:
        print("I'm trader!")
        return 1000000
