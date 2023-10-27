from pydub import AudioSegment

original = AudioSegment.from_wav('beat.wav')
print(type(original))
print(original)

reversed = original.reverse()

reversed += 15  #add 15 more dB

##issue with ffmpeg
reversed.export('reversed_beat.wav')

#get fraction of the audio: units =  milliseconds
first_two_seconds = original[0:2000]
first_two_seconds.export('first_two_seconds_beat.wav')

#merge audio_files
merged = original * 2 + AudioSegment.silent(1000) + reversed
merged.export('merged_beat.wav')
