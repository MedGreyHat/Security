""" facebook loginform cracker """
import mechanize

b = mechanize.Browser()
target = "https://www.facebook.com/login.php?login_attempt=1"
response = b.open(target)

b.select_form(nr = 0) # select form name from html file
b.form['email'] = 'moh2012peace@hotmail.fr'
b.form['pass'] = '#NoviceCoder2018#'
b.method = "POST"
response = b.submit()

print response.geturl()


