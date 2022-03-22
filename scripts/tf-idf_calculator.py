import pymorphy2
import re
from nltk.corpus import stopwords

doc_path = '../documents/doc'
token_freq_path = '../tokens_frequencies/doc'
lemma_freq_path = '../lemmas_frequencies/doc'

index_file = open('../inverted_index.txt', 'r', encoding='utf-8')
index_lines = index_file.read().split('\n')
index = dict()
for index_line in index_lines:
    pair = index_line.split(': ')
    index[pair[0]] = [int(ind) for ind in pair[1].split(' ')]

lemmas_file = open('../lemmas.txt', 'r', encoding='utf-8')
lemmas_lines = lemmas_file.read().split('\n')
lemmas = dict()
lemmas_index = dict()
for lemmas_line in lemmas_lines:
    pair = lemmas_line.split(': ')
    for lemma in pair[1].split(' '):
        lemmas_index[lemma] = []

N = 200
stops = stopwords.words('russian')
morph = pymorphy2.MorphAnalyzer()

for i in range(1, N+1):
    doc = open('{}{}.txt'.format(doc_path, str(i)), 'r', encoding='utf-8')
    content = doc.read()
    doc.close()
    words = [w for w in re.findall(r'[а-я]+', content.lower()) if w not in stops and len(w) > 2]
    for word in words:
        lemmas_index[word].append(i)

for i in range(1, N+1):
    doc = open('{}{}.txt'.format(doc_path, str(i)), 'r', encoding='utf-8')
    content = doc.read()
    doc.close()
    words = [w for w in re.findall(r'[а-я]+', content.lower()) if w not in stops and len(w) > 2]
    n = len(words)
    tokens_freqs = dict((t, 0) for t in index.keys())
    lemmas_freqs = dict((l, 0) for l in lemmas_index.keys())
    for word in words:
        tokens_freqs[morph.parse(word)[0].normal_form] += 1
        lemmas_freqs[word] += 1
    tokens_freq_file = open('{}{}.txt'.format(token_freq_path, str(i)), 'a', encoding='utf-8')
    for token in index.keys():
        tf = float(tokens_freqs[token] / n)
        idf = float(len(index[token]) / N)
        tokens_freq_file.write("{} {} {}\n".format(token, tf, idf))
    tokens_freq_file.close()
    lemmas_freq_file = open('{}{}.txt'.format(lemma_freq_path, str(i)), 'a', encoding='utf-8')
    for lemma in lemmas_index.keys():
        tf = float(lemmas_freqs[lemma] / n)
        idf = float(len(lemmas_index[lemma]) / N)
        lemmas_freq_file.write("{} {} {}\n".format(lemma, tf, idf))
    lemmas_freq_file.close()