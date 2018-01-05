""" Browse the Web annonymosly """
import mechanize, cookielib, random, time

class AWB(mechanize.Browser):
    def __init__(self, proxies=[], user_agents=[]):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)
        self.proxies = proxies
        self.user_agents = user_agents + ['Mozilla/5.0', 'FireFox/6.01', 'ExactSearch'\
                                         'Nokia7110/10']
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)                                    
        self.anonymize()
    
    def clear_cookies(self):
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
    
    def change_user_agent(self):
        index = random.randrange(0, len(self.user_agents))
        self.addheaders = [('User-agent', self.user_agents[index])]
    
    def change_proxy(self):
        if self.proxies:
            index = random.randrange(0, len(self.proxies))
            self.set_proxies =({'http':self.proxies[index]})
    
    def anonymize(self, sleep = False):
        self.clear_cookies()
        self.change_user_agent()
        self.change_proxy()
        if sleep:
            time.sleep(60)

""" Test Unit """
ab = AWB(user_agents=[('User-agent', 'superSecretBrowser')])
for attempt in range(1, 5):
    ab.anonymize()
    print "[*] Fetching page"
    response = ab.open('https://www.youtube.com')
    for coockie in ab.cookie_jar:
        print cookie