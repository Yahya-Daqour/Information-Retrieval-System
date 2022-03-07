import math
from collections import OrderedDict

def inverse_document_frequency(Dataframe):
    postingList = dict()
    wordFreq = dict()
    for index, row in Dataframe.iterrows():
        for word in row[0]:
            postingList.setdefault(word, set()).add(index)
        for word in row[1]:
            postingList.setdefault(word, set()).add(index)
        for word in row[2]:
            postingList.setdefault(word, set()).add(index)
        for word in row[3]:
            postingList.setdefault(word, set()).add(index)

    # sort elements
    #postingList = OrderedDict(sorted(postingList.items()))
    for key, value in postingList.items():
        wordFreq[key] = math.log(1400 / len(value))

    # converting the dictionaries into tuple
    postingList = [(k, v) for k, v in postingList.items()]
    wordFreq = [(k, v) for k, v in wordFreq.items()]
    for i in range(len(postingList)):
        postingList[i] = list(postingList[i])
        postingList[i].insert(1, wordFreq[i][1])
    return postingList

def tf_idf_weighting(Dataframe, postingList):
    tf = dict()
    wordFreq = dict()
    for i in range(len(postingList)):
        countFreq = 0
        for index in postingList[i][2]:
            countInDoc = 0
            for col in range(4):
                text = Dataframe.iloc[index, col]
                for word in text:
                    if word == postingList[i][0]:
                        countInDoc += 1
                        countFreq += 1

            tf_weight = math.log2(1 + countInDoc)
            tf_idf = tf_weight * postingList[i][1]  # tf-idf = log2(1 + term frequency) * log( number of documents /  document frequency)
            tf.setdefault(postingList[i][0], {}).update({index: tf_idf})
            wordFreq[postingList[i][0]] = countFreq


    return tf, wordFreq