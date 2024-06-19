from configparser import ConfigParser
import logging
from config.default_parameters import INI_FILE_PATH
config = ConfigParser()
logger = logging.getLogger(__name__)

def update_config_ini(section, key, value):
    logger.info('update config_ini')
    config.read(INI_FILE_PATH)
    config[section][key] = value
    
    with open(INI_FILE_PATH, 'w') as f:
        config.write(f)
        