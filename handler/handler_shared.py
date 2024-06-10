from configparser import ConfigParser
from config.default_parameters import INI_FILE_PATH
config = ConfigParser()

def update_config_ini(section, key, value):
    config.read(INI_FILE_PATH)
    config[section][key] = value
    
    with open(INI_FILE_PATH, 'w') as f:
        config.write(f)
        