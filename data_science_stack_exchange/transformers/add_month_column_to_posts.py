import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from data_science_stack_exchange.utils.helpers.transformers import add_month_column


@transformer
def transform(data, *args, **kwargs):
    return add_month_column(data, 'CreationDate', 'CreationMonth')


@test
def test_output(df, *args) -> None:
    assert df is not None, 'The output is undefined'
    assert df.dtypes['CreationMonth'] == pd.StringDtype()
