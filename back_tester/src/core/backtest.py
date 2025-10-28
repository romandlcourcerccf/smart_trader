from abc import ABC, abstractmethod
from typing import Sequence, Dict, Any

from .strategy import AbstractStrategy


class BackTestResult(ABC):
    pass


class AbstractBackTestSystem(ABC):
    @abstractmethod
    def run_backtest(
        self, strateries: Sequence[AbstractStrategy]
    ) -> Dict[str, Dict[str, Any]]:
        pass


class TestBackTestSystem(AbstractBackTestSystem):
    def run_backtest(self, strateries):
        result = {}

        for strategy in strateries:
            result[strategy.id] = self._run_for_strategy(strategy)

        return result

    def _run_for_strategy(sel, strategy):
        return {"PNL": 1.0, "SharpeRatio": 3.0}
