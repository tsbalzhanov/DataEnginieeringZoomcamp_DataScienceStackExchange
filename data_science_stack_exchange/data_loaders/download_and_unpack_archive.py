import pathlib
import tempfile

import pyunpack
import requests
from tqdm import tqdm

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def requests_streaming_download(url: str) -> bytes:
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with io.BytesIO() as buffer, tqdm(total=total, unit='iB', unit_scale=True, unit_divisor=1024) as bar:
        for data in resp.iter_content(chunk_size=128*1024):
            buffer.write(data)
            bar.update(len(data))
        return buffer.getvalue()


def download_and_unpack_archive(url: str, output_dir_path: pathlib.Path | str) -> None:
    output_dir_path = pathlib.Path(output_dir_path)
    output_dir_path.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = pathlib.Path(temp_dir) / 'file'
        with temp_file_path.open('wb') as temp_file:
            print(f'Downloading {url}')
            response = requests.get(url, stream=True)
            response_size= int(response.headers.get('content-length', 0))
            with tqdm(total=response_size, unit='iB', unit_scale=True, unit_divisor=1024) as bar:
                for data in response.iter_content(chunk_size=512*1024):
                    temp_file.write(data)
                    bar.update(len(data))
        pyunpack.Archive(temp_file_path).extractall(output_dir_path)


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    url = 'https://archive.org/download/stackexchange/datascience.meta.stackexchange.com.7z'

    data_dir = pathlib.Path(kwargs['DATA_DIR'])
    data_dir.mkdir(exist_ok=True)
    download_and_unpack_archive(url, data_dir)
    return str(data_dir)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
