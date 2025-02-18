from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

def getdata(driver, url):

    driver.get(url)
    dataDic = {}
    dataDic["url"] = url
    # Initialize variables
    instagram_link=""
    dis_name = ""
    #short_info = ""
    region = ""
    founded = ""
    owner = ""
    status = ""
    website = ""
    open_for_visits = ""
    capacity = ""
    types = ""
    cereals = ""
    water = ""
    longitude = ""
    latitude = ""

    try:
        info = driver.find_element(By.CLASS_NAME, "rightmapbox")
        links = info.find_elements(By.TAG_NAME, "a")
        hrefs = [link.get_attribute("href") for link in links]
        instagram_link_ = next((href for href in hrefs if "instagram.com" in href), None)
        dataDic["instagram_link"] = instagram_link_
        #print(instagram_link)

        infotext=info.text
        info_lines = infotext.split('\n')
        dist_name_ = info_lines[0]
        dataDic["dis_name"] = dist_name_
       # short_info_ = info_lines[1] if "The" in info_lines[1] else ""
       # dataDic["short_info"] = short_info_
        region_ = ""
        founded_ = ""
        owner_ = ""
        status_ = ""
        website_ = ""
        open_for_visits_ = ""
        capacity_ = ""
        types_ = ""
        cereals_ = ""
        water_ = ""

        for line in info_lines:
            
            if "Region :" in line:
                region_ = line.replace("Region :", "").strip()
                dataDic["region"] = region_
            if "Founded :" in line:
                founded_ = line.replace("Founded :", "").strip()
                dataDic["founded"] = founded_   
            if "Owner :" in line:
                owner_ = line.replace("Owner :", "").strip()
                dataDic["owner"] = owner_
            if "Status :" in line:    
                status_ = line.replace("Status :", "").strip()
                dataDic["status"] = status_
            if "Website :" in line:    
                website_ = line.replace("Website :", "").strip()
                dataDic["website"] = website_
            if "Open for visits :" in line:
                open_for_visits_ = line.replace("Open for visits :", "").strip()
                dataDic["open_for_visits"] = open_for_visits_
            if "Capacity :" in line:
                capacity_ = line.replace("Capacity :", "").strip()
                dataDic["capacity"] = capacity_
            if "Types :" in line:
                types_ = line.replace("Types :", "").strip()
                dataDic["types"] = types_
            if "Cereals :" in line:
                cereals_ = line.replace("Cereals :", "").strip()
                dataDic["cereals"] = cereals_
            if "Water :" in line:
                water_ = line.replace("Water :", "").strip()
                dataDic["water"] = water_
      
    except Exception as e:
        print("Element not found")

    try:
        # Wait until the "Improve this map" link is present
        improve_map_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.mapbox-improve-map"))
        )

        # Extract the href attribute (URL)
        mapbox_feedback_url = improve_map_link.get_attribute("href")
        #print("Mapbox Feedback URL:", mapbox_feedback_url)

        match = re.search(r'#/([-.\d]+)/([-.\d]+)/\d+', mapbox_feedback_url)

        if match:
            longitude_, latitude_ = match.groups()
            dataDic["longitude"] = longitude_
            dataDic["latitude"] = latitude_
            #print("Longitude:", longitude)
            #print("Latitude:", latitude)
        else:
            print("Coordinates not found in URL")

    except Exception as e:
        print("Error:", e)


    return dataDic
       