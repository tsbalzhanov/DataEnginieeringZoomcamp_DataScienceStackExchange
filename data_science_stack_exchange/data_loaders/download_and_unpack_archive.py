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
    data_dir = pathlib.Path(kwargs['DATA_DIR'])
    data_dir.mkdir(exist_ok=True)
    download_and_unpack_archive(kwargs['INITIAL_DATA_URL'], data_dir)
    return {'data_dir': str(data_dir)}


@test
def test_output(data_dir_dict, *args) -> None:
    assert data_dir_dict is not None, 'The output is undefined'
    assert 'data_dir' in data_dir_dict
    data_dir_path = pathlib.Path(data_dir_dict['data_dir'])
    assert data_dir_path.exists() and data_dir_path.is_dir()
    assert set((file_.name for file_ in data_dir_path.iterdir())) ==\
        {'Badges.xml', 'Comments.xml', 'PostHistory.xml', 'PostLinks.xml', 'Posts.xml', 'Tags.xml', 'Users.xml', 'Votes.xml'}
