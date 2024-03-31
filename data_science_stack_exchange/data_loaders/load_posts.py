import pathlib

import pandas as pd

from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from data_science_stack_exchange.utils.helpers.loaders import load_and_parse_dataframe


@data_loader
def load_data_from_file(data_dir_dict: dict, **kwargs):
    data_dir_path = pathlib.Path(data_dir_dict['data_dir'])
    return load_and_parse_dataframe(
        data_dir_path / 'Posts.xml',
        {
            'Body': pd.StringDtype(),
            'Title': pd.StringDtype(),
            'Tags': pd.StringDtype(),
            'ContentLicense': pd.StringDtype(),
            'OwnerDisplayName': pd.StringDtype(),
            'ParentId': 'Int64',
            'ViewCount': 'Int64',
            'AnswerCount': 'Int64',
            'AcceptedAnswerId': 'Int64',
            'LastEditorUserId': 'Int64',
            'FavoriteCount': 'Int64'
        },
        ['CreationDate', 'LastActivityDate', 'LastEditDate', 'CommunityOwnedDate', 'ClosedDate']
    )


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
