import pymorphy2
import re
from nltk.corpus import stopwords

doc_path = 'documents/doc'
tokens_file = open('../tokens.txt', 'a', encoding='utf-8')
tokens = set()
lemmas = dict()
stops = stopwords.words('russian')
morph = pymorphy2.MorphAnalyzer()
for i in range(1, 201):
    doc = open('{}{}.txt'.format(doc_path, str(i)), 'r', encoding='utf-8')
    content = doc.read()
    words = [w for w in re.findall(r'[а-я]+', content.lower()) if w not in stops and len(w) > 2]
    for word in words:
        token = morph.parse(word)[0].normal_form
        if token not in lemmas.keys():
            tokens.add(token)
            lemmas[token] = set()
            tokens_file.write('{}\n'.format(token))
        lemmas[token].add(word)
    doc.close()
tokens_file.close()
lemmas_file = open('../lemmas.txt', 'a', encoding='utf-8')
for token in tokens:
    lemmas_file.write('{}:'.format(token))
    for t in lemmas[token]:
        lemmas_file.write(' {}'.format(t))
    lemmas_file.write('\n')
lemmas_file.close()