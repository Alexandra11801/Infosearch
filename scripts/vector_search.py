import os
import webbrowser
import pymorphy2
import re
import numpy as np
from nltk.corpus import stopwords

html_path = 'file://' + os.path.realpath('../pages/page')
token_freq_path = '../tokens_frequencies/doc'
request = input()
stops = stopwords.words('russian')
morph = pymorphy2.MorphAnalyzer()
req_words = [w for w in re.findall(r'[а-я]+', request.lower()) if w not in stops and len(w) > 2]
req_tokens = set([morph.parse(w)[0].normal_form for w in req_words])
results_count = 5
doc_count = 200
results = [np.empty(1) for i in range(doc_count)]
for i in range(doc_count):
    results[i][0] = i + 1
    freq_file = open('{}{}.txt'.format(token_freq_path, str(i + 1)), 'r', encoding='utf-8')
    freq_content = freq_file.read()
    freq_file.close()
    for token in req_tokens:
        match = re.search(rf'{token}\s\d+\.\d+\s\d+\.\d+', freq_content)
        if match:
            freq_line = match.group()
            splited = freq_line.split(' ')
            relevancy = float(splited[1]) / float(splited[2])
        else:
            relevancy = 0
        results[i] = np.append(results[i], relevancy)
results = [res for res in results if 0 not in res[1:]]
results = sorted(results, key=lambda res: np.linalg.norm(res[1:]), reverse = True)
for i in range(min(results_count, len(results))):
    url = '{}{}.html'.format(html_path, int(results[i][0]))
    webbrowser.open_new_tab(url)