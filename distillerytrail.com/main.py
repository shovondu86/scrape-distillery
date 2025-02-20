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

# def main():
#     dataDic = {}
#     for i in range(9, 14):  
#         print(i)
#         try:
#             link_list = link_extract.getlink(driver, i)
#             for href in link_list:
#                 print(href)
#                 dataDic["url"] = href

#                 #dataList = data_extract.getdata(driver, href)
#                 #print(dataList)
#                 data_append.append_to_csv(dataDic)
#         except Exception as e:
#             print(f"An error occurred: {e}")

def main():
    csv_file = "distillerytrail.com\WhiskeyMaps - Attributes1.csv"

    # Open and read the CSV file
    with open(csv_file, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row.get("url"))
            data_list=data_extract.getdata(driver, row.get("url"))
            data_append.append_to_csv(data_list)

if __name__ == "__main__":
    main()

