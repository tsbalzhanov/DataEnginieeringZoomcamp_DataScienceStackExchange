import os
import pathlib

from mage_ai.io.config import ConfigKey

from .mage_env import load_config


def setup_google_cloud_credentials(config_profile='default') -> None:
    config = load_config(config_profile)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config[ConfigKey.GOOGLE_SERVICE_ACC_KEY_FILEPATH]
