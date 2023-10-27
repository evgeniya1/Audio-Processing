from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')
beat_low = beat.low_pass_filter(2000)  #frequency = 2000
beat_low.export('beat_low.wav', format='wav')

#mono speaker: #-1 - left, 1 - right, but it is continuous
beat_left = beat_low.pan(-1)
beat_right = beat_low.pan(1)

beat_left.export('beat_left.wav', format='wav')

beat_final = beat_left + beat_right + beat_low
beat_final.export('beat_final.wav', format='wav')