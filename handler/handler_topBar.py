import logging

logger = logging.getLogger(__name__)

def handle_toggle_menu(main_window, isChecked):
    logger.info('handler called')
    main_window.widget_sideExpanded.setHidden(isChecked)
    main_window.widget_sideShrinked.setVisible(isChecked)
