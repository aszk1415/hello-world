import requests
import parsel
import csv

urls = [f'http://yibian.hopto.org/fang/?fno={i+1}'for i in range(73,150)]
# print(url)
def get_res(url):
    res = requests.get(url)
    res.encoding ='big5'
# print(res.text)
    selector = parsel.Selector(res.text)
    return selector

def craw(selector):
    name = ''
    component = []
    dose = []
    combine= []
    provenance = ''
    lis = selector.xpath('//td[@class="content_board"]/p/a/text()')
    le = selector.xpath('//td[@class="content_board"]/p/font/text()')
    an = selector.xpath('//td[@class="content_board"]/table[1]/tr/th[1]/text()')
    fr = selector.xpath('//td[@class="content_board"]/table[1]/tr/th[2]/a/text()')
    name = an.get()
    provenance = fr.get()
    combine.append(name)
    combine.append(provenance)
    for li in lis:
        component.append(li.get())
    for l in le:
        dose.append(l.get())
    for num in range(len(component)):
        combine.append(f'{component[num]}({dose[num]})')
    with open('方劑.csv',mode='a',encoding='utf-8',newline='')as f:
        csv_write = csv.writer(f)
        csv_write.writerow(combine)
#     print(name,provenance,combine)

   for url in urls:
    sel = get_res(url)
    craw(sel)
