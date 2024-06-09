from PySide6.QtWidgets import QFileDialog
from os import path
from configparser import ConfigParser
from config.default_parameters import INI_FILE_PATH
from config.sections import SECTION_SETTINGS_TAB_1
config = ConfigParser()


def handle_browse_path(target_object, key):
    """Set the target_object's text to user browse path.

    Args:
        target_object (Any): any QObject that has setText()
    """
    directory = QFileDialog.getExistingDirectory(
        target_object.window(), 'Select default directory')
    if directory:
        config.read(INI_FILE_PATH)
        config[SECTION_SETTINGS_TAB_1][key] = directory
        with open(INI_FILE_PATH, 'w') as f:
            config.write(f)
        target_object.setText(directory)
