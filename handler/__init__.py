"""Handler module initialization."""

from .handler_main import (handle_backward, handle_btn_library_populate,
                           handle_end_of_media, handle_forward, handle_mute,
                           handle_next, handle_page_switch, handle_play_order,
                           handle_player, handle_populate_table_song,
                           handle_prev, handle_slider_progress_pressed,
                           handle_slider_progress_released,
                           handle_slider_volume_changed,
                           handle_spinning_bocchi_clicked, handle_toggle_menu,
                           handle_track_paused, handle_track_played,
                           handle_track_position_changed, handle_track_stopped)
from .handler_page_download import (handle_check_audio_only,
                                    handle_check_include_thumbnail,
                                    handle_check_use_default_path,
                                    handle_download_track)
from .handler_page_library import handle_le_search_bar
from .handler_page_settings import handle_browse_path
from .handler_shared import *
