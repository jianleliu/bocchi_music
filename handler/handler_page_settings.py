"""handler for settings page."""
import logging
from configparser import ConfigParser

from PySide6.QtWidgets import QFileDialog

from config.default_parameters import INI_FILE_PATH, DEFAULT_ENCODING
from config.sections import SECTION_SETTINGS_TAB_1

config = ConfigParser()
logger = logging.getLogger(__name__)


def handle_browse_path(target_object: "any qt object with setText()", key: str):
    """Set the target_object's text to user browse path. update ini file.

    Args:
        target_object (Any): any QObject that has setText()
        key (str): key constant of ini file.
    """
    directory = QFileDialog.getExistingDirectory(
        target_object.window(), 'Select default directory')
    if directory:
        config.read(INI_FILE_PATH)
        config[SECTION_SETTINGS_TAB_1][key] = directory
        with open(INI_FILE_PATH, 'w', encoding=DEFAULT_ENCODING) as f:
            config.write(f)
        target_object.setText(directory)
