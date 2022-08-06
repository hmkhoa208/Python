from selenium import webdriver
from bs4 import BeautifulSoup
import time



# Lay BeautifulSoup cua website
def getSoup(site):
	driver = webdriver.Firefox()
	# driver.maximize_window()
	driver.get(site)
	time.sleep(2)
	soup = BeautifulSoup(driver.page_source,'lxml')
	driver.quit()
	return soup


#----------------------------------------

if __name__ == '__main__':
    # with open("html_result.html", "w") as file:
    #     file.write(str(getSoup('https://www.youtube.com/')))
    soup = getSoup('https://www.google.com/')
    print(soup.find('title').text)
