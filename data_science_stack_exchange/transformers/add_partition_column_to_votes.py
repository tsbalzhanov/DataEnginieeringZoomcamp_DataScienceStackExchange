import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from data_science_stack_exchange.utils.helpers import transformers as transformers_helpers


@transformer
def transform(df, *args, **kwargs):
    return transformers_helpers.add_post_partition_column(df, 'PostId', **kwargs)


@test
def test_output(df, *args, **kwargs) -> None:
    assert df is not None, 'The output is undefined'
    assert df.dtypes['PostIdPartition'] == int
