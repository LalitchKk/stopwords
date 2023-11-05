import re

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


#stop word
def getstopWords(text):
    stop_words = set(stopwords.words('english'))
    review = re.sub('@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+', ' ', text)
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in stop_words]
    review = ' '.join(review)
    return review
