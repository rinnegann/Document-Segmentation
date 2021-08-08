import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
# options = webdriver.ChromeOptions()
# options.headless = True
# driver = webdriver.Chrome(options=options)
#Read Text File
with open("structure-detection-data-set.txt","r") as f:
    #Read a Line withought \n
    lines = [line.strip() for line in f.readlines()]
# print(data.shape)
working_urls = []
bad_urls = []
time_out_url = []
for URL in lines:
    try:
        res = requests.get(URL,timeout=30)
        working_urls.append(URL)
        print("This web url is working")
        continue
    except requests.ConnectionError as e:
        print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
        print(str(e))
        bad_urls.append(URL)            
        continue
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        time_out_url.append(URL)
        print(str(e))
        continue
    except requests.RequestException as e:
        print("OOPS!! General Error")
        print(str(e))
        continue
    except KeyboardInterrupt:
        print("Someone closed the program")  
    #
print(f"Working Url are {working_urls}")
print()
print(f"Technical error {bad_urls}")
print()
print(f"Time out url {time_out_url}")


#For Getting Full Screen Shot
# count = 0
# driver = webdriver.Chrome(os.getcwd()+"\chromedriver.exe")
# 
# for actual_url in working_urls:
#         driver.get(actual_url)
#         S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
#         driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
#         driver.find_element_by_tag_name('body').screenshot(f'web_screenshot_{count}.png')
#         count+=1
# driver.quit()