# download one file

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import urllib.request

try:
    browser = webdriver.Firefox()
    browser.get("https://finance.yahoo.com/quote/4151.T/history?period1=946652400&period2=1575558000&interval=1d&filter=history&frequency=1d")
    elem = browser.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/section/div[1]/div[2]/span[2]/a")
                                        　# 同じURL でもボットがアクセスすると XPATH が変わる  /html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[2]/span[2]/a
    print(elem)
    download_url = elem[0].get_attribute("href")
    print("URL:: " + download_url)
    urllib.request.urlretrieve(download_url, "\\_YahooFinance.csv")
    time.sleep(3) 

except Exception as ex:
    print(ex)
 
#browser.close()


