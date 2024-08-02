import pytube

link = 'https://www.youtube.com/watch?v=1_lInOGL-SA&list=RDGMEMCMFH2exzjBeE_zAHHJOdxg&start_radio=1&rv=_4lNiafQ-Pk'
p = pytube.Playlist(link)
print(p.title)