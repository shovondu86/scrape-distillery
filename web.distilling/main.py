from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data_extract
import data_append
import csv
from urllib.parse import unquote

service = Service(r'C:\chromedriver-win64\chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=service, options=chrome_options)

def main():
    csv_file = 'urls.csv'

    # Open and read the CSV file
    with open(csv_file, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row.get("url"))
            data_list=data_extract.getdata(driver, row.get("id"),str(row.get("url")))
            #print(data_list)
            data_append.append_to_csv(data_list)
            



    
if __name__ == "__main__":
    main()



