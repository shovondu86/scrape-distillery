from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data_extract
import data_append

service = Service(r'C:\driver\chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=service, options=chrome_options)

data_list=data_extract.getdata(driver, "https://whiskey-map.com/distillery/borders/61")
data_append.append_to_csv(data_list)
#print(data_list)

# driver.get("https://whiskey-map.com/distillery/borders/61")
# #https://whiskey-map.com/distillery/borders/61
# #https://whiskey-map.com/distillery/cameronbridge/766





