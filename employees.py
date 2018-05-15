#https://stackoverflow.com/questions/33876657/how-to-install-python-any-version-in-windows-when-youve-no-admin-priviledges
import requests
from lxml import html
import os
import datetime
import time
import re
from requests_ntlm import HttpNtlmAuth
import sys
sys.path.append('../')
from mylib import auth

#Для подавления сообщения "InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised."
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
'''
url = 'http://net.open.ru/common/auth.php'
payload = {}
payload['from'] = 'L3J1L3NlYXJjaC9pbmRleC5waHA/cTQ9MzQ1JnNvcnQ0PTEmdHlwZV9zdWJfZGl2aXNpb240PSZzdWJfZGl2aXNpb240PQ=='
'''
url = 'http://net.open.ru/ru/search/index.php'
payload = {}
search = 'Родионов'
search = search.encode('cp1251')
#payload['q4'] = 'Родионов Сергей Анатольевич'
payload['q4'] = search

try:
    s = requests.Session()
    s.auth = HttpNtlmAuth(auth('ntlm')['login'],auth('ntlm')['password'])

    r = s.get(url, verify=False, params=payload)
    if r.status_code != requests.codes.ok:
        raise http_error
except:
    print(r.status_code) 
    raise SystemExit

tree = html.fromstring(r.text)
empl = tree.xpath('//div[@class = "search-result-rows"]//div[@class = "row"]')

empl_fio = tree.xpath('//div[@class = "employee-data-fio"]/text()')
empl_email = tree.xpath('//div[@class = "employee-email ec"]/a/span/text()')
empl_phone = tree.xpath('//div[@class = "employee-phone ec"]/text()')

for e in empl:
    print(e.xpath('//div[@class = "employee-data-fio"]/text()'))
    print(e.xpath('//div[@class = "employee-email ec"]/a/span/text()'))
    print(e.xpath('//div[@class = "employee-phone ec"]/text()'))

#print(r.text)
#f = open('out.csv','w', newline="")
#columns = ["fio", "email", "phone"]
#writer = csv.DictWriter(file, fieldnames=columns)
#writer.writeheader()

#f.write(r.text)
#f.close()