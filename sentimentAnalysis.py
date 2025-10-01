"""
Analysizes sentiment of an article with AI using the TextBlob library.

Based on a tutorial : https://www.youtube.com/watch?v=tXuvh5_Xyrw
Modified/extended by Nicholas Schwartz
"""

import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')
nltk.download('punkt_tab')

mathmatics_article_url = "https://en.wikipedia.org/wiki/Mathematics"
math_article = Article(mathmatics_article_url)

math_article.download()
math_article.parse()
math_article.nlp()   

text = math_article.text 

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # score from -1 to 1 (where 1 is most positive and -1 is most negative)
#Should be close to 0 since wikipedia is meant to be impartial
print("Mathmatics article sentiment: ", sentiment)
negative_article_url = "https://www.bbc.com/news/world-us-canada-58514967"
negative_article = Article(negative_article_url)

negative_article.download()
negative_article.parse()
negative_article.nlp()   

text = negative_article.text

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
#should be close to -1
print("Negative article sentiment: ", sentiment)

positive_article_url = "https://www.yahoo.com/entertainment/celebrity/articles/julianne-hough-recalls-everything-fell-185607526.html"
positive_article = Article(positive_article_url)

positive_article.download()
positive_article.parse()
positive_article.nlp()   

text = positive_article.text

blob = TextBlob(text)
sentiment = blob.sentiment.polarity 
print("Positive article sentiment: ", sentiment)
