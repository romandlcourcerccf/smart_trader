from src.core.backtest import TestBackTestSystem
from src.core.strategy import EmptyStrategy_1, EmptyStrategy_2


def test_backtest():
    es1 = EmptyStrategy_1()
    es2 = EmptyStrategy_2()

    ts = TestBackTestSystem()

    stratigies = [es1, es2]

    res = ts.run_backtest(stratigies)

    assert len(res) == len(stratigies)
