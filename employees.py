#https://stackoverflow.com/questions/33876657/how-to-install-python-any-version-in-windows-when-youve-no-admin-priviledges
import requests
from lxml import html
import os
import datetime
import time
import re
from requests_ntlm import HttpNtlmAuth

#Для подавления сообщения "InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised."
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'http://net.open.ru/common/auth.php'
payload = {}
payload['from'] = 'L3J1L3NlYXJjaC9pbmRleC5waHA/cTQ9MzQ1JnNvcnQ0PTEmdHlwZV9zdWJfZGl2aXNpb240PSZzdWJfZGl2aXNpb240PQ=='

'''
url = 'http://net.open.ru/ru/search/index.php'
payload = {}
payload['q4'] = 'Родионов Сергей Анатольевич'
'''
try:
    s = requests.Session()
    s.auth = HttpNtlmAuth('open.ru\\','')    
    r = s.get(url, verify=False, params=payload)
    if r.status_code != requests.codes.ok:
        raise http_error
except:
    print(r.status_code) 
    raise SystemExit

print(r.text)