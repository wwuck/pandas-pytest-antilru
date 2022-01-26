import pandas as pd


def test_basic_csv():
    result = pd.read_csv('test.csv')

    assert result == 1
