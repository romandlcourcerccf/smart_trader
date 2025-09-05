from src.core.system import SimpleTrader


def test_run_session():
    trader = SimpleTrader()
    assert trader.run_session() > 0
