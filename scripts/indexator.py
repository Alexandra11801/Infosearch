import pymorphy2
import re
from nltk.corpus import stopwords

stops = stopwords.words('russian')
morph = pymorphy2.MorphAnalyzer()
tokens_file = open('../tokens.txt', 'r', encoding='utf-8')
tokens = tokens_file.read().split('\n')
tokens_file.close()
index = dict((token, []) for token in tokens)
doc_path = '../documents/doc'
for i in range(1, 201):
    doc = open('{}{}.txt'.format(doc_path, str(i)), 'r', encoding='utf-8')
    content = doc.read()
    doc.close()
    words = [w for w in re.findall(r'[а-я]+', content.lower()) if w not in stops and len(w) > 2]
    for word in words:
        token = morph.parse(word)[0].normal_form
        if i not in index[token]:
            index[token].append(i)
index_file = open('../inverted_index.txt', 'a', encoding='utf-8')
for token in index.keys():
    index_file.write('{}:'.format(token))
    for doc_num in index[token]:
        index_file.write(' {}'.format(doc_num))
    index_file.write('\n')
index_file.close()