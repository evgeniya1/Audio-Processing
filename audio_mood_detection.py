from speech_recognition import Recognizer, AudioFile
from nltk.sentiment import SentimentIntensityAnalyzer

# import nltk
# nltk.download('vader_lexicon')

recognizer = Recognizer()

with AudioFile('chile.wav') as audio_file:
  audio = recognizer.record(audio_file)

chile_text = recognizer.recognize_google(audio)
print(chile_text)

analyzer = SentimentIntensityAnalyzer()

print(analyzer.polarity_scores(chile_text))

sentiment = 'Positive' if analyzer.polarity_scores(
    chile_text)['compound'] > 0 else 'Negative'
print('\n', sentiment, 'Speech')
