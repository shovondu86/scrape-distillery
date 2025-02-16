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

for i in range(10, 14):  
    print(i)
    try:
        link_list = link_extract.getlink(driver, i)
        for href in link_list:
            dataList = data_extract.getdata(driver, href)
            #print(dataList)
            data_append.append_to_csv(dataList)
    except Exception as e:
        print(f"An error occurred: {e}")



# dataList=data_extract.getdata(driver,"https://www.distillerytrail.com/directory-distillery/listing/boone-county-distilling/")
# print(dataList)

# def appedn_to_csv(dataList):
#     # open CSV file and read header
#     with open("WhiskeyMaps - Attributes.csv", "r") as f:
#         reader = csv.reader(f)
#         for header in reader:
#             break

#     # add row to CSV file
#     try:90
#         with open("WhiskeyMaps - Attributes.csv", "a", newline='') as f:
#             writer = csv.DictWriter(f, fieldnames=header)
#             writer.writerow(dataList)
#     except Exception as e:
#         print(f"Error appending to CSV: {e}")



# driver.get("https://www.distillerytrail.com/directory-distillery/?_page=1&sort=post_title")

# # Find the div with the specified class
# div = driver.find_element(By.CLASS_NAME, "drts-view-entities-list-grid")
# #print(div.text)

# # Find all anchor tags within the div
# links = div.find_elements(By.TAG_NAME, "a")

# # Extract the href attributes
# hrefs = [link.get_attribute("href") for link in links]

# # Print the hrefs
# unique_hrefs = list(set(href for href in hrefs if 'listing' in href))

# for href in unique_hrefs:
#     print(href)

driver.quit()
