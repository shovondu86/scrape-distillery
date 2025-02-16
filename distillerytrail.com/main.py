from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import link_extract
import data_extract
import csv
import data_append

service = Service(r'C:\driver\chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=service, options=chrome_options)

def main():
    for i in range(1, 14):  
        print(i)
        try:
            link_list = link_extract.getlink(driver, i)
            for href in link_list:
                dataList = data_extract.getdata(driver, href)
                #print(dataList)
                data_append.append_to_csv(dataList)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

