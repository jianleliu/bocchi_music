import logging

logger = logging.getLogger(__name__)

def handle_page_switch(window: object, page_num: int):
    window.widget_pageManager.setCurrentIndex(page_num)
    window.widget_pageManager.show()
    window.widget_videoWidget.hide()