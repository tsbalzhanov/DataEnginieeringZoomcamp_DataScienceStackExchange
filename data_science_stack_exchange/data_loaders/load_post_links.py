import pathlib

import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from data_science_stack_exchange.utils.helpers.loaders import load_and_parse_dataframe


@data_loader
def load_data(data_dir_dict: dict, **kwargs):
    data_dir_path = pathlib.Path(data_dir_dict['data_dir'])
    return load_and_parse_dataframe(
        data_dir_path / 'PostLinks.xml',
        {},
        ['CreationDate']
    )


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
