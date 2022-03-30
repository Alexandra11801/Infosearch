doc_path = '../documents/doc'
html_path = '../pages/page'
for i in range(1, 201):
    doc = open('{}{}.txt'.format(doc_path, str(i)), 'r', encoding='utf-8')
    content = doc.read()
    doc.close()
    page = open('{}{}.html'.format(html_path, str(i)), 'a', encoding='utf-8')
    page.write(content)
    page.close()