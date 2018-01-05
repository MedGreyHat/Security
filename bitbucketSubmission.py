""" Submit to bitbucket website using python """
import request
from lxml import html

USERNAME = "<your user_name here>"
PASSWORD = "<your password here>"

LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
URL = "https://bitbucket.org/dashboard/overview"

def main():
    session_requests = requests.session()
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
    payload = {
        "username":USERNAME,
        "password":PASSWORD,
        "csrfmiddlewaretoken":authenticity_token
    }
    # make the login
    result = session_requests.post(LOGIN_URL, data= payload, headers = dict(referer = LOGIN_URL))
    # scrape the url
    result = session_requests.get(URL, headers = dict(referer = URL)) 
    tree = html.fromstring(result.content)
    bitbucket_names = tree.path("//dix[@class = 'repo-list--repo']/a/text()")
    
    print bitbucket_names

if __name__ == "__main__":
    main()



