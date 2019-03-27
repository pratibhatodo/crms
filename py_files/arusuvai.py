from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
x = '1'
sys.setdefaultencoding('utf-8')
browser = webdriver.Chrome()
url = 'http://www.arusuvai.com/recipes/appetizers/'
browser.get((url))
html_container = browser.find_element_by_id("block-system-main" ).get_attribute('innerHTML')
if html_container is not None:
	soup = BeautifulSoup(html_container, 'html.parser')
	product = soup.findAll("div", {"class": "views-field views-field-title"}, recursive=True)
	if product is not None:
		for product in product:
			name = product.find("span", {"class": "field-content"}, recursive=True)
			if name is not None:
				link = name.find("a", recursive=True)
				print link.text
				print link['href']

		next_url = url+'?type=All&veg_or_non_veg=All&page='+x
		print next_url





			