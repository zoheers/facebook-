from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time


class Face:
    browser = None

    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument('--dns-prefetch-disable')
        firefox_options.add_argument('--no-sandbox')
        firefox_options.add_argument('--lang=en-US')
        self.browser = webdriver.Firefox(executable_path=r'D:\geckodriver', firefox_options=firefox_options)
        self.browser.get(r"https://m.facebook.com/")

    def login(self,mail,pas):
        print ("login start...")
        signup_elem = self.browser.find_element_by_name('email')
        signup_elem.send_keys(mail)
        login_elem = self.browser.find_element_by_name('pass')
        login_elem.send_keys(pas)

        login_elem =self.browser.find_element_by_name("login")
        login_elem.click()
        print ("login finish...")

    def post_group(self, url, message):
        self.browser.get(url)
        time.sleep(5)
        # do actual commenthow are you)
        ins = self.browser.find_element_by_name('xc_message')
        ins.send_keys(message)

    def add_photo(self, url, path, txt):
        self.browser.get(url)
        ins = self.browser.find_element_by_name('view_photo')
        ins.click()
        ins = self.browser.find_element_by_name("file1")
        ins.send_keys(r"C:\Users\D\Desktop\1.png")
        ins = self.browser.find_element_by_name("add_photo_done")
        ins.click()
        ins = self.browser.find_element_by_name("view_post")
        ins.click()
        ins = self.browser.find_element_by_name("done")
        ins.click()
