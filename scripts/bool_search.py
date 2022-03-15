import pymorphy2
import re

index_file = open('../inverted_index.txt', 'r', encoding='utf-8')
index_lines = index_file.read().split('\n')
index = dict()
for index_line in index_lines:
    pair = index_line.split(': ')
    index[pair[0]] = [int(ind) for ind in pair[1].split(' ')]
query = str(input())
words = [w for w in re.findall(r'[а-я]+', query.lower())]
morph = pymorphy2.MorphAnalyzer()
for word in words:
    token = morph.parse(word)[0].normal_form
    indices = index[token]
    query = query.replace(word, '(i in {})'.format(indices))
result = []
doc_count = 200
equation = 'result = [i for i in range({}) if {}]'.format(doc_count, query)
exec(equation)
print(result)