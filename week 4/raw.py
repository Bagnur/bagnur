import re

filemile = open(r'raw.txt', 'r', encoding='utf-8')
f = filemile.read()
name=re.search('Филиал\sТОО\s[\w]+\s\w+', f)
binmin =re.search('\d{12}', f)
title=re.findall('\d+\.+\n(.*)', f)
cnt = re.findall('\d,\d{3}', f)
price= re.findall('\d,\d{3}\sx\s(.*)',f)
total = re.findall('Стоимость\n(.*)', f)
date = re.search('\d\d\.\d\d.*', f)
adres = re.search('г\..*',f)
print('Name of the company: ' + name.group())
print('BIN number: ' + binmin.group())

for i in range(len(title)):
    print("title: " + title[i])
    print("cnt: " + cnt[i])
    print("price: " + price[i])
    print('total: ' + total[i])

print('Date: ' + date.group())
print('Address: '+ adres.group())
