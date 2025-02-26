from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from urllib.parse import unquote

def getdata(driver, id, url):

    driver.get(url)
    dataDic = {}
    dataDic["id"] = id
   
    ##Social Media Links

    try:
        info_soc = driver.find_element(By.CLASS_NAME, "ListingDetails_Level3_SOCIALMEDIA")
        links = info_soc.find_elements(By.TAG_NAME, "a")
        hrefs = [link.get_attribute("href").replace("https://web.distilling.com/external/wcpages/referral.aspx?URL=", "") for link in links]
        
        xtwitter = next((link for link in hrefs if "twitter.com" in link or "x.com" in link), "")
        instagram = next((link for link in hrefs if "instagram.com" in link), "")
        tiktok = next((link for link in hrefs if "tiktok.com" in link), "")
        social_link_ = [unquote(xtwitter), unquote(instagram), unquote(tiktok)]
        #print(social_link_)
        dataDic["social_link"] = social_link_
    except Exception as e:
        print("Social Media Links Error")
        

    ##founded 
    try:
        info_found = driver.find_elements(By.CLASS_NAME, "ListingDetails_Level3_CUSTOMFIELDS")[0]
        foundate_ = info_found.text.replace("Year Established: ", "")
        #print(foundate_)
        dataDic["founded"] = foundate_

    except:
        print("Fonded error")

    ##cerificate
    try:
        info_lic = driver.find_elements(By.CLASS_NAME, "ListingDetails_Level3_CUSTOMFIELDS")[1]
        cerificate_= info_lic.text
        #print(cerificate_)
        dataDic["cerificate"] = cerificate_
        
    except:
        print("Certificate error")

    ##website
    try:
        info_web = driver.find_element(By.CLASS_NAME, "ListingDetails_Level3_VISITSITE")
        website_ = info_web.find_element(By.TAG_NAME, "a").get_attribute("href")
        #print(website_)
        dataDic["website"] = website_
    except:
        print("Website error")

    ##owner
    try:
        info_owner = driver.find_element(By.CLASS_NAME, "ListingDetails_Level3_MAINCONTACT").text
        info_owner_ = info_owner.split("\n")[0]
        #print(info_owner_)
        dataDic["owner"] = info_owner_

        
    except:
        print("owner error")

    ##Amenities, capcity, tourse
    production_vol= ['Commercial','Macro','Micro','Nano']
    amenities_list = [
            "Bar or Cocktail Lounge",
            "Distillery - Brewery",
            "Distillery - Cidery",
            "Distillery - Winery",
            "Events and Music",
            "Lodging",
            "Restaurant",
            "Tasting Room",
            "Tours"
        ]


    try:
        info_amenities = driver.find_element(By.CLASS_NAME, "ListingDetails_Level3_AFFILIATIONS")
        images = info_amenities.find_elements(By.TAG_NAME, "img")
        image_titles = [image.get_attribute("title") for image in images]
        capacity_ = [title for title in image_titles if title in production_vol]
        amenities_ = [title for title in image_titles if title in amenities_list]
        open_for_visits_= "Yes" if "Tours" in amenities_ else ""
        dataDic["capacity"] = capacity_
        dataDic["amenities"] = amenities_
        dataDic["open_for_visits"] = open_for_visits_

        
    except:
        print("Amenities error")


    return dataDic
       