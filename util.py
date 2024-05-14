from pytube import YouTube, Playlist
import os
import json 

def download_mp3(video_url, directory=os.getcwd(), audio_only=True):
  print(f'url: {video_url} directory: {directory}')
  yt = YouTube(video_url)
  stream = yt.streams.filter(only_audio=True).first()
  stream.download(output_path=directory)
  
  file_path = stream.get_file_path()
  # data = None
  # # read json content
  # with open('config.json', 'r') as f:
  #       data = json.load(f)
  
  # # construct new song entity
  # new_song_index = len(data['songs']) + 1
  # new_song = {
  #     'num_played': 0,
  #     'path': file_path,
  # }
  # data['songs'][str(new_song_index)] = new_song

  # # write to json
  # with open('config.json', 'w') as f:
  #     json.dump(data, f, indent=4) 
  return file_path
    
  
def download_playlist(playlist_url, directory='.', audio_only=True): 
  pass

def init_song_table(songs_dir=os.getcwd(), extension=['.mp4']) -> dict:
  song_table = {} # filename: path
  if not os.path.isdir(songs_dir):
    return song_table
  
  for filename in os.listdir(songs_dir):
    if any(filename.endswith(ext) for ext in extension):
      song_table[os.path.splitext(filename)[0]] = os.path.join(songs_dir, filename)
  return song_table

def init_config_file():
  if not (os.path.exists('config.json') and (os.path.getsize('config.json') > 0)):
    with open('config.json', 'w') as f:
      json.dump({
        'songs': {},
        'preferences': {},
        'playlists': {}
        }, f, indent=4)