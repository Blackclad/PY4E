import socket

#promt the user for a URL
try:
    url = input('Enter a valid URL:  ')
except:
    print('invalid URL')

#Split the URL into protocol / domain / page
furl = url.split('/')

#Select only the domain..
fdom = furl[2]

#Print only the domain, just to see if the split worked, this will be inserted in mysock.connect...
print(fdom)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((fdom, 80))
#mysock.connect(('data.pr4e.org', 80))
cmd = 'GET '+url+'HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(1024)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()