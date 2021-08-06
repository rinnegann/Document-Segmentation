# """This file is get screen shot of full web pages and save it jpeg images"""
# from selenium import  webdriver
# import os
# from PIL import Image
# import  time


# driver = webdriver.Chrome()
# # driver.get("https://www.youtube.com")

# url = "http://zakon3.rada.gov.ua/laws/show/77-19"

# driver.get(url)

# # driver.execute_script("document.body.style.zoom='50%'")
# # driver.set_window_size(1920,1080,driver.window_handles[0])
# # driver.maximize_window()
# driver.save_screenshot("image_3.png")

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'http://zakon3.rada.gov.ua/laws/show/77-19'

driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

driver.quit()