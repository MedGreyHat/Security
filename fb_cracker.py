#_*_coding:utf_8_*_
from oauth_tokens.providers.facebook import FacebookAuthRequest
req = FacebookAuthRequest(username='username_here', password='password_here')
response = req.authorized_request(url='https://facebook.com')
response.content.count('username_here')
fileobj = open("HTML-OUTPUT.txt","wb")
fileobj.write(response.content)
fileobj.close()
