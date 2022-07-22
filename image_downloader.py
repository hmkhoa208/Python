from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from PIL import Image
from lxml import html 
import time
import json
import os

# Lay BeautifulSoup cua website
def getSoup(site):
	driver = webdriver.Firefox()
	# driver.maximize_window()
	driver.get(site)
	time.sleep(5)
	soup = BeautifulSoup(driver.page_source,'lxml')
	driver.quit()
	return soup

def downloadImage(url, name):
    img_data = requests.get(url).content
    with open(name + '.webp', 'wb') as handler:
        handler.write(img_data)
    im = Image.open(name + '.webp').convert('RGB')
    im.save(name + '.jpg', 'jpeg')
    os.remove(name + '.webp')

if __name__ == '__main__':
    page = getSoup('https://www.youtube.com/c/RelaxationFilm/videos')
    # tree = html.fromstring(str(page))
    # img_src_list = tree.xpath('//*[@id="img"]/@src')
    img_arr = page.find_all(id='img')
    img_src_list = []
    for img in img_arr:
        if img.has_attr('src'):
            img_src_list.append(img['src'])
    count = 1
    for img in img_src_list:
        print(img)
        downloadImage(img, str(count))
        count = count + 1
    # with open('html.html', 'w') as file:
    #     file.write(html.tostring(element))
