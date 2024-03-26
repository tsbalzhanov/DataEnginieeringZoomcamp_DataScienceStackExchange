import pathlib

import pandas as pd

from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from data_science_stack_exchange.utils.helpers import loaders_common


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    return loaders_common.load_and_parse_dataframe(
        pathlib.Path(kwargs['DATA_DIR']) / 'Posts.xml',
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
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
