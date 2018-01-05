#_*_coding:utf_8_*_
from oauth_tokens.providers.facebook import FacebookAuthRequest
req = FacebookAuthRequest(username='Mohamed El Général', password='#NoviceCoder2018#')
response = req.authorized_request(url='https://facebook.com')
response.content.count('Mohamed El Général')
fileobj = open("HTML-OUTPUT.txt","wb")
fileobj.write(response.content)
fileobj.close()