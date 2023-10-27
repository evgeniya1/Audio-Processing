from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')
sax = AudioSegment.from_wav('sax.wav')

print(len(beat), len(sax))

beat2 = beat * 2

mixed = beat2.overlay('mixed.wav')

final = beat2 + mixed * 2 + sax + beat2 + sax

final.export('final.wav')