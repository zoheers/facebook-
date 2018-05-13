from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

firefox_options = Options()
firefox_options.add_argument('--dns-prefetch-disable')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--lang=en-US')
browser = webdriver.Firefox(executable_path=r'D:\geckodriver', firefox_options=firefox_options)


browser.get('https://www.facebook.com/')
time.sleep(5)
lan = browser.find_elements_by_tag_name('a')
for x in lan:
    print (x.text)
    if 'English (US)' in x.text.strip():
        x.click()
        break
time.sleep(2)

signup_elem = browser.find_element_by_id('email')
signup_elem.send_keys('+1(479)345-0537')

login_elem = browser.find_element_by_id('pass')
login_elem.send_keys('0555514650')

ins = browser.find_elements_by_tag_name('input')
for x in ins:
    if x.get_attribute('value') == 'Log In':
        x.click() # here logged in
        print ("log in")
        break
#then key here move to mobile version as that doesn't support javascript
time.sleep(3)
browser.get('https://m.facebook.com')
'''el = browser.find_element_by_name('query')
el.send_keys('antony white')
el.send_keys(Keys.ENTER)
sleep(3)'''

temp= ''
ak = browser.find_elements_by_tag_name('a')
for a in ak:
    if a.get_attribute('href').endswith('search'):
        a.click()
        temp = a.get_attribute('href')[:a.get_attribute('href').find("?")]
        break

# CLICK TIMELINE
browser.get(r'https://m.facebook.com/ahmad.hayaty.7/posts/105967116945988')
time.sleep(10)


# find last post (occurance of comment)
as_el = browser.find_elements_by_tag_name('a')
for a in as_el:
    print(a.text)
    if 'omment' in a.text.strip():
        a.click()
        break
time.sleep(10)


# do actual comment
ins = browser.find_element_by_name('comment_text')
ins.send_keys('Best cars !')
# submit input
ins = browser.find_elements_by_tag_name('input')
for x in ins:
    if 'Comment' in x.get_attribute('value'):
        if x.get_attribute('value')!= "Mention friends in this comment":
            x.click()
            break
