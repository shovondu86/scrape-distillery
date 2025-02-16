from selenium.webdriver.common.by import By

def getdata(driver, url):

    driver.get(url)
    dataDic = {}

    # Initialize variables
    dis_name = ""
    location = ""
    trail = ""
    spirit_class = ""
    address = ""
    latitude = ""
    longitude = ""
    phone = ""
    email = ""
    website = ""
    social_link = ""
    found_date = ""
    certificate = ""
    amenities = ""

    #Distillery Name
    try:
        dis_name_ = driver.find_element(By.CLASS_NAME, "jupiterx-main-header-post-title").text
        print(dis_name_)
        dataDic["dis_name"] = dis_name_
        
    except Exception as e:
        print("Element not found: Distillery Name")
        

    #location, trail, spirit_class
    try:
        info = driver.find_element(By.CLASS_NAME, "drts-display-element-column-5")
        infotext = info.text
        info_lines = infotext.split('\n')
        info_lines_filtered = [line for line in info_lines if "Featured" not in line]
        location_ = info_lines_filtered[0]
        trail_ = info_lines_filtered[1]
        spirit_class_ = info_lines_filtered[2]
        #print(location,trail,spirit_class)
        #dataDic["location","trail","spirit_class"] = location_,trail_,spirit_class_
        dataDic["location"] = location_
        dataDic["trail"] = trail_
        dataDic["spirit_class"] = spirit_class_


    except Exception as e:
        print("Element not found: location, trail, spirit_class")
        

    #Adrress, Latitude, Longitude
    try:
        info2 = driver.find_element(By.CLASS_NAME, "drts-display-element-column-11")
        location_address = info2.find_element(By.CLASS_NAME, "drts-map-marker-trigger")
        location_address_url = location_address.find_element(By.TAG_NAME, "a").get_attribute("href")
        coordinates = location_address_url.split("query=")[-1].split(",")
        latitude_ = coordinates[0]
        longitude_ = coordinates[1]
        address_ = location_address.text
        #print(latitude,longitude,address)
        #dataDic["address","latitude","longitude"] = address_,latitude_,longitude_
        dataDic["address"] = address_
        dataDic["latitude"] = latitude_
        dataDic["longitude"] = longitude_


    except Exception as e:
        print("Element not found: Adrress, Latitude, Longitude")
        

    #Phone, Email
    try:
        info3 = driver.find_element(By.CLASS_NAME, "drts-display-element-group-8")
        info_lines3 = info3.text.split('\n')
        info_lines_filtered3 = [line for line in info_lines3]
        phone_ = info_lines_filtered3[0]
        email_ = info_lines_filtered3[1]
        #print(phone,email)
        #dataDic["phone","email"] = phone_,email_
        dataDic["phone"] = phone_
        dataDic["email"] = email_

    except Exception as e:
        print("Element not found: Phone, Email")
      

    #Website, Twitter, Instagram, Tiktok
    try:
        info4 = driver.find_element(By.CLASS_NAME, "drts-display-element-group-7")
        infolinks4 = info4.find_elements(By.TAG_NAME, "a")
        infohrefs4 = [link.get_attribute("href") for link in infolinks4]
        website_ = infohrefs4[0]
        xtwitter= next((link for link in infohrefs4 if "twitter.com" in link or "x.com" in link), "")
        instagram = next((link for link in infohrefs4 if "instagram.com" in link), "")
        tiktok = next((link for link in infohrefs4 if "tiktok.com" in link), "")
        social_link_ = [xtwitter,instagram,tiktok]
        #print(website_,social_link_)
        #dataDic["website","social_link"] = website_,social_link_
        dataDic["website"] = website_
        dataDic["social_link"] = social_link_

    except Exception as e:
        print("Element not found: Website, Twitter, Instagram, Tiktok")
        

    #Founding Date/cerificate
    try:
        info5 = driver.find_element(By.CLASS_NAME, "drts-display-element-group-6")
        info5Text5 = info5.text

        info5TextSplit5 = info5Text5.split('\n')
       
        found_date_ = next((line.split("Founded")[-1].strip() for line in info5TextSplit5 if "Founded" in line), "")
        certificate_ = next((line.split('/')[-1].strip() for line in info5TextSplit5 if "DSP" in line), "")
        #print(found_date,certificate)
        #dataDic["found_date","certificate"] = found_date_,certificate_ 
        dataDic["found_date"] = found_date_
        dataDic["certificate"] = certificate_       
    except Exception as e:
        print("Element not found: Founding Date/lic")
        

    #Amenities
    try:
        info6 = driver.find_element(By.CLASS_NAME, "drts-display-element-entity_field_field_features-1")
        infotext6 = info6.text
        amenities_ = [line for line in infotext6.split('\n') if "Amenities" not in line]
        #print(amenities)
        dataDic["amenities"] = amenities_
    
    except Exception as e:
        print("Element not found: Amenities")

    return dataDic
       