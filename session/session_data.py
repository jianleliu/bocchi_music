"""store session data parameters such as song_entity dict. exports session_data."""
from config.default_parameters import DEFAULT_PLAY_ORDER
from config.keys import KEY_DICT_PLAYER_STATES_PLAY_ORDER
from initialization.initialization_external import initialize_external
from initialization.initialization_internal import generate_dict_song_entity


class _SessionData():
    """session data instance. stores session data parameters.
    """

    def __init__(self) -> None:
        initialize_external()
        self.initialize_variables()

    def initialize_variables(self):
        """initialize session data parameters.
        """
        self.dict_song_entity = generate_dict_song_entity()
        self.dict_player_states = {
            KEY_DICT_PLAYER_STATES_PLAY_ORDER: DEFAULT_PLAY_ORDER,

        }


session_data = _SessionData()
