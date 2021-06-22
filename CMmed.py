import requests
import parsel

res = requests.get('http://yibian.hopto.org/fang/?fno=1')
res.encoding ='big5'
print(res.text)
selector = parsel.Selector(res.text)

name = ''
component = []
dose = []

lis = selector.xpath('//td[@class="content_board"]/p/a/text()')
le = selector.xpath('//td[@class="content_board"]/p/font/text()')
an = selector.xpath('//td[@class="content_board"]/table[1]/tr/th[1]/text()')
name =an.get()

for a in n :
    name.append(a.get())
for li in lis:
    component.append(li.get())
for l in le:
    dose.append(l.get())
print(component)
print(dose)
print(name)
