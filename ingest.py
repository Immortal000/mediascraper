import eyed3 as eyed3
import magic

audiofile = eyed3.load("test-mp3.mp3")
audiofile.initTag()
audiofile.tag.artist = u"Integrity"
audiofile.tag.album = u"Humanity Is The Devil"
audiofile.tag.album_artist = u"Integrity"
audiofile.tag.title = u"Hollow"
audiofile.tag.track_num = 2
