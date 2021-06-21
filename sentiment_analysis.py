import nltk
analyzer = nltk.sentiment.SentimentIntensityAnalyzer()
def main():
    while True:
        user_text = input("?")
        score = get_sentiment(user_text)
        reaction = get_reaction(score)
        print(reaction)
        print(score)
        print(" ")

def get_reaction(score):
    if score > 0.5:
        return ""
    if score > 0:
        return ""
    if score == 0.5:
        return ""
    if score < -0.5:
        return ""
    if score < 0.5:
        return ""

def get_sentiment(user_text):
    scores = analyzer.polarity_scores(user_text)
    sentiment_score = scores["compound"]
    return sentiment_score

if __name__ == "__main__":
    main()