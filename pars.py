import requests
import lxml.html

#В этом файле представлены два кода, которые обращаются к разным страницам сайта

"""Вариант парсинга со страницы Python Events
    Дополнительно выводим место проведения события с помощью f-строки
    А так же дату проведения"""

html = requests.get('https://www.python.org/events/python-events/').content

tree = lxml.html.document_fromstring(html)
events = tree.xpath('/html/body/div/div[3]/div/section/div/div/ul/li')
for li in events:
    event = (li.find('h3/a')).text
    place = (li.find('p/span')).text
    date = (li.find('p/time')).text
    print(f'"{event}" in {place}, date: {date}')

print('\n')

"""Вариант парсинга с главной страницы сайта"""
html = requests.get('https://www.python.org').content

tree = lxml.html.document_fromstring(html)
events = tree.xpath('/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li')
for li in events:
    a = li.find('a')
    print(a.text)
