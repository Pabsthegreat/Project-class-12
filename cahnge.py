from os import path
from pydub import AudioSegment

src = "themesong.mp3"
dst = "theme1.wav"

sound = AudioSegment.from_mp3(src)
sound.export(dst, format = "wav")