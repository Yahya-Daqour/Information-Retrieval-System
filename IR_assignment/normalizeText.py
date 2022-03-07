import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def normalize_text(text):
    stop = stopwords.words('english')
    ps = PorterStemmer()
    # remove short words
    text = re.sub(r'\b\w{1,3}\b', '', text)
    # remove punkt
    text = "".join(i for i in text if i not in ("?", ".", ";", ":", "!", "$", "'", '"', ",", "-", "_", "{", "}", "[", "]", "(", ")", "*", "+", "=", "/"))
    # remove numbers
    text = ''.join(i for i in text if not i.isdigit())
    # perform stemming and remove stop words
    text_tokens = word_tokenize(text)
    text_filtered = [ps.stem(word) for word in text_tokens if ps.stem(word) not in stop]
    text = " ".join(text_filtered)
    # remove short words
    text = re.sub(r'\b\w{1,3}\b', '', text)
    # token the sentence
    text = word_tokenize(text)
    return text