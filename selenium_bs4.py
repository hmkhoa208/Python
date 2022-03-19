from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

# Lay BeautifulSoup cua website
def getSoup(site):
	driver = webdriver.Firefox()
	# driver.maximize_window()
	driver.get(site)
	time.sleep(5)
	soup = BeautifulSoup(driver.page_source,'lxml')
	driver.quit()
	return soup


#----------------------------------------

if __name__ == '__main__':
	# Enter your login credentials here
	print(getSoup('https://www.google.com/'))

