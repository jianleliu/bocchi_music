"""handler for library page"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget


def handle_le_search_bar(table_song: QTableWidget, text: str) -> None:
    """filter song table based on search bar text.

    Args:
        table_song (QTableWidget): song table instancem ui.
        text (str): le_search_bar text.
    """
    all_items = table_song.findItems('.', Qt.MatchFlag.MatchRegularExpression)
    matched_items = table_song.findItems(
        text, Qt.MatchFlag.MatchContains | Qt.MatchFlag.MatchFixedString)
    rows_to_hide = []
    rows_to_show = []

    for item in all_items:
        row = table_song.row(item)
        rows_to_hide.append(row)

    for item in matched_items:
        row = table_song.row(item)
        rows_to_show.append(row)

    for row in rows_to_hide:
        table_song.setRowHidden(row, True)

    for row in rows_to_show:
        table_song.setRowHidden(row, False)
