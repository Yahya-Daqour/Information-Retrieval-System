import pandas as pd
from frequency import inverse_document_frequency, tf_idf_weighting
from statistics import get_num_token, get_num_single, most_freq
from normalizeText import normalize_text

# read the files
df = pd.read_json('/home/yahyadaqour/IR_assignment/venv/Data/cranfield_data.json')
df.drop('id', axis='columns', inplace=True)

quer = pd.read_csv('smallqueries.csv', names=['queries'])


# Part A

# normalize text and tokenize the words
df['author'] = [normalize_text(text) for text in df.author.values]
df['bibliography'] = [normalize_text(text) for text in df.bibliography.values]
df['body'] = [normalize_text(text) for text in df.body.values]
df['title'] = [normalize_text(text) for text in df.title.values]
quer = [normalize_text(text) for text in quer.queries.values]

# Part B
# Document Frequency
wordFreq = dict()
# The list of documents containing the term
postingList = ()
postingList = inverse_document_frequency(df)
# term frequency
termFreq = dict()
termFreq, wordFreq = tf_idf_weighting(df, postingList)
print('number of tokens : ')
print(get_num_token(df))
print('number of unique words : ')
print(len(postingList))
print('number of single words: ')
print(get_num_single(wordFreq))
print("The 30 most frequent words :")
most_freq(wordFreq, termFreq)
print('average number of word tokens per document:')
print(get_num_token(df)/1400)

