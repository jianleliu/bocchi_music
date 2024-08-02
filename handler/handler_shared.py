"""helper functions"""
from configparser import ConfigParser
import logging
from config.default_parameters import INI_FILE_PATH, DEFAULT_ENCODING
config = ConfigParser()
logger = logging.getLogger(__name__)


def update_config_ini(section: str, key: str, value: str) -> None:
    """update config ini file. constants can be found in config/.

    Args:
        section (str): section constant.
        key (str): key constant.
        value (str): new value.
    """
    logger.info('update config_ini')
    config.read(INI_FILE_PATH)
    config[section][key] = value

    with open(INI_FILE_PATH, 'w', encoding=DEFAULT_ENCODING) as f:
        config.write(f)
