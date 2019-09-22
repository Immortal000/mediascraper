from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

mp3 = MP3File("audio.mp3")
mp3.set_version(VERSION_BOTH)
print(mp3.album)
string = "i am dumb"
mp3.album = string
print(mp3.album)
tags = mp3.get_tags()
print(tags)
mp3.save




