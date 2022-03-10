import random
import urllib.request
import urllib.error

path = 'https://www.labirint.ru/books/'
doc_path = 'documents\\doc'
index_file = open('index.txt', 'a')
i = 1
while i <= 200:
    index = random.randint(1,500000)
    url = path+str(index)+'/'
    try:
        page = urllib.request.urlopen(url)
        doc = open(doc_path+str(i)+'.txt', 'w', encoding='utf-8')
        doc.write(page.read().decode('utf8'))
        doc.close()
        index_file.write('{}. {}\n'.format(i, url))
        i += 1
    except (urllib.error.HTTPError, ConnectionResetError):
        continue
index_file.close()