import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = input('Enter count: ')
posit = input('Enter position: ')

lst = []

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    lst.append(tag)
    print(tag.get('href', None))

print(lst[posit])