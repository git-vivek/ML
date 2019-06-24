#!/usr/bin/python3

import cgi
print("COntent-type: text/html\n")
#from InstagramAPI import InstagramAPI
#import moviepy
web=cgi.FieldStorage()
username=web.getvalue('x')
password=web.getvalue('y')
from instapy_cli import client

#username = passwd
#password = user
image = '/home/rashi/Downloads/a393800bfd5da67df615b0278796bf65.jpg'
text = 'This will be the caption of your photo.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

with client(username, password) as cli:
        cli.upload(image, text)

