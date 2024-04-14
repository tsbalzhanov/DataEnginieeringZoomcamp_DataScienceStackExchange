import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from data_science_stack_exchange.utils.helpers import transformers as transformers_helpers


@transformer
def transform(df, *args, **kwargs):
    transformers_helpers.add_post_partition_column(df, 'PostId', **kwargs)
    transformers_helpers.add_user_partition_column(df, 'UserId', **kwargs)
    return df


@test
def test_output(df, *args, **kwargs) -> None:
    assert df is not None, 'The output is undefined'
    assert df.dtypes[kwargs['POST_ID_PARTITIONS_COLUMN']] in (int, pd.Int64Dtype())
    assert df.dtypes[kwargs['USER_ID_PARTITIONS_COLUMN']] in (int, pd.Int64Dtype())
