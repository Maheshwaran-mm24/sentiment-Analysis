import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob
df = pd.read_csv('amazon_grocery_Data.csv')
df['Sentiment_grcry'] = df['review_headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)