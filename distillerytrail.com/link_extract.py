from selenium.webdriver.common.by import By

def getlink(driver,page):
   
    url = "https://www.distillerytrail.com/directory-distillery/?_page=" + str(page) + "&sort=post_title"
    driver.get(url)
    div = driver.find_element(By.CLASS_NAME, "drts-view-entities-list-grid")
    
    links = div.find_elements(By.TAG_NAME, "a")

    hrefs = [link.get_attribute("href") for link in links]

    unique_hrefs = list(set(href for href in hrefs if 'listing' in href))

    # for href in unique_hrefs:
    #     print(href)

    return unique_hrefs
