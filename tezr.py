import fhn
from fhn import Cam
from selenium import webdriver

s= Cam()
s.drive.get(r"http:\\www.google.com")
a = s.drive.find_element_by_id("lst-ib")
a.send_keys("vd")