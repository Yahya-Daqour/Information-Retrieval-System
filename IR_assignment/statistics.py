def get_num_token(Dataframe):
    count = 0
    for index, row in Dataframe.iterrows():
        for col in Dataframe:
            for word in row[col]:
                count += 1
    return count

def get_num_single(dic):
    count = 0
    for word in dic:
        if dic[word] == 1:
            count += 1
    return count

def most_freq(wordFreq, termFreq):
    sorted_dic = {}
    sorted_keys = sorted(wordFreq, key=wordFreq.get)
    for word in sorted_keys:
        sorted_dic[word] = wordFreq[word]

    for i in range(1, 31):
        i = len(wordFreq) - i
        print(i-len(sorted_dic), 'Term :', list(sorted_dic)[i], '\t\tFrequency :', sorted_dic[list(sorted_dic)[i]], '\nTF :', termFreq[list(sorted_dic)[i]])
