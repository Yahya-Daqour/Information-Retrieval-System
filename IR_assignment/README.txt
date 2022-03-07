This program was made for Information Retrieval System to work in Natural Language Processing (NLP) using PyCharm IDE.

First, The program reads cranfield data file (json format) and puts into a data-frame using pandas library, after that we start to clean the data by removing short words, punctuations, and numbers.

Then, we use NLTK library to tokenize the words, remove the stop words and perform stemming (NOTE: the word will be removed if it becomes a stop word after stemming), functions are registered at "normalize_text.py".

Next, we determine the document frequency and make a posting list, merge them together into a tuple and the data looks like this(['word', document frequency, {document id}]).

After that, from the posting list we access the document id's and calculate how many times the term occurs in that document, functions are registered at "frequency.py".

Finally, the number of tokens after preprocess, the number of unique words, single words,the 30 most frequent words alongside their respective information and the average number of words tokens will be printed, functions are registered at "statistics.py".

**************************

If you want to run the program, just edit the path of cranfiled_data  (in main.py) and you are ready to go.
