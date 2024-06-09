import re

# Regex for YouTube song (video)
video_regex = re.compile(r'^(https?:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/(watch\?v=|embed\/|v\/|.+\?v=)?([A-Za-z0-9_-]{11})$')

# Regex for YouTube playlist
playlist_regex = re.compile(r'list=')

def check_youtube_url(url):
    if video_regex.match(url):
        return "song"
    elif playlist_regex.findall(url):
        return "playlist"
    else:
        return "invalid"

# Test URLs
urls = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Video
    "https://youtu.be/dQw4w9WgXcQ",  # Shortened Video URL
    "https://www.youtube.com/playlist?list=PLynGq5yST4E0btwLznAjm7KxSp8UKlC_G",  # Playlist
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLynGq5yST4E0btwLznAjm7KxSp8UKlC_G",  # Video in Playlist
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be",  # Video with extra parameter
    "https://www.youtube.com/embed/dQw4w9WgXcQ",  # Embedded Video
    'https://www.youtube.com/watch?v=Y7jskzeZsa4&list=RDMMY7jskzeZsa4&start_radio=1',
    'https://www.youtube.com/watch?v=_4lNiafQ-Pk&list=PL54TaQc-CFCqnq6LVo2yII4y1OzMggnZV&index=1'
]

for url in urls:
    print(f"{url}: {check_youtube_url(url)}")
