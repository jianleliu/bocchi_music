from initialization.initialization_internal import generate_dict_song_entity
from config.default_parameters import *
from config.keys import *
from config.sections import *
from initialization.initialization_external import *

class SessionData():
  def __init__(self) -> None:
    initialize_external()
    self.initialize_variables()
  
  def initialize_variables(self):
    self.dict_song_entity = generate_dict_song_entity()
    self.dict_player_states = {
        KEY_DICT_PLAYER_STATES_PLAY_ORDER: DEFAULT_PLAY_ORDER,

    }
    
    
session_data = SessionData()