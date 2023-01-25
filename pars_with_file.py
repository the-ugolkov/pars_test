import lxml.html
from lxml import etree

#В этом файле представлены два одинаковых фрагмента кода, которые обращаются к html файлам страниц сайта

"""Обращение к главной странице сайта"""
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())

ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li')
for li in ul:
    a = li.find('a')
    print(a.text)

print('\n')

"""Обращение к целевой странице сайта"""
tree = etree.parse('Our Events | Python.org.html', lxml.html.HTMLParser())

ul = tree.findall('/body/div/div[3]/div/section/div/div/ul/li/h3')
for li in ul:
    a = li.find('a')
    print(a.text)
