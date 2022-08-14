import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def soupcan(s):
    html = urllib.request.urlopen(s, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return(tags)

tags = soupcan(input('Parent URL - '))
que = input('Number of links - ')
linknum = input('Search position in link order - ')

while que != 0:
    que = int(que) - 1
    newtag = tags[int(linknum) - 1].get('href', None)
    print(tags[int(linknum) - 1].contents[0])
    tags = soupcan(newtag)