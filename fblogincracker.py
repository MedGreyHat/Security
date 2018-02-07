""" facebook loginform cracker """
import mechanize

b = mechanize.Browser()
target = "https://www.facebook.com/login.php?login_attempt=1"
response = b.open(target)

b.select_form(nr = 0) # select form name from html file
b.form['email'] = 'email_here'
b.form['pass'] = 'password_here'
b.method = "POST"
response = b.submit()

print response.geturl()


