import random
import urllib.request
import urllib.error

path = 'https://www.labirint.ru/books/'
docPath = 'documents\\doc'
indexFile = open('index.txt', 'a')
i = 1
while i <= 200:
    index = random.randint(1,500000)
    url = path+str(index)+'/'
    try:
        page = urllib.request.urlopen(url)
        doc = open(docPath+str(i)+'.txt', 'w', encoding='utf-8')
        doc.write(page.read().decode('utf8'))
        doc.close()
        indexFile.write('{}. {}\n'.format(i, url))
        i += 1
    except (urllib.error.HTTPError, ConnectionResetError):
        continue
indexFile.close()