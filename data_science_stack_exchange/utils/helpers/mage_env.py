import os
import pathlib

from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader


def load_config(config_profile='default') -> None:
    config_path = pathlib.Path(get_repo_path()) / 'io_config.yaml'
    return ConfigFileLoader(config_path, config_profile)
