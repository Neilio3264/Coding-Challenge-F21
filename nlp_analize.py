from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

sia = SentimentIntensityAnalyzer()
f = open("input.txt", "r")
text = f.read()

sent = sent_tokenize(text)
print(sent)
print("\n\n")

for sentence in sent:
    sent_score = sia.polarity_scores(sentence)
    print("For sentence, [", sentence, "] score is:", sent_score)
    print()
print("\n\n")

score = sia.polarity_scores(text)
print("Overall sentiment score is:", score)