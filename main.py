from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
import pandas as pd
import time
import os


DELAY = 1

OK = True

while OK:

    user_answer = input("Rent or buy: ").lower()

    if user_answer == "rent":
        min_bed = input("Minimum beds: ")
        max_rent = input("Maximum rent: ")
        URL = f"https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=OUTCODE%5E2497" \
              f"&minBedrooms={min_bed}&maxPrice={max_rent}" \
              f"&radius=1.0&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords="


    elif user_answer == "buy":
        min_bed = input("Minimum beds: ")
        max_price = input("Maximum price: ")
        URL = f"https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=OUTCODE%5E2497" \
              f"&minBedrooms={min_bed}&maxPrice={max_price}&radius=0.5&propertyTypes=&includeSSTC=false&mustHave=" \
              f"&dontShow=&furnishTypes=&keywords="
    else:
        URL = f"https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=" \
              f"OUTCODE%5E2497&minBedrooms=1&maxPrice=10000" \
              f"&radius=0.25&propertyTypes=&maxDaysSinceAdded=1&mustHave=&dontShow=&furnishTypes=&keywords="

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    time.sleep(DELAY)

    # Obtain total number of pages in the website
    page = 1
    pages_search = driver.find_element(By.XPATH, '//*[@id="l-container"]/div[3]/div/div/div/div[2]/span[3]').text
    total_pages = int(pages_search)

    # Create list to fill with selenium
    list_properties_address = []
    list_properties_info = []
    list_properties_link = []
    list_properties_price = []

    while page <= total_pages:

        all_properties_address = driver.find_elements(By.CLASS_NAME, "propertyCard-address")
        all_properties_info = driver.find_elements(By.CLASS_NAME, "property-information")
        all_properties_link = driver.find_elements(By.CLASS_NAME, "propertyCard-priceLink")
        all_properties_price = driver.find_elements(By.CLASS_NAME, "propertyCard-priceValue")

        for n in all_properties_address:
            list_properties_address.append(n.text)

        for n in all_properties_info:
            list_properties_info.append(n.text)

        for n in all_properties_link:
            list_properties_link.append(n.get_attribute("href"))

        for n in all_properties_price:
            n_split = n.text.split("£")[1]
            n_split2 = n_split.split(" ")[0]
            n_split3 = n_split2.split(",")
            n_final = int("".join(n_split3))
            list_properties_price.append(n_final)

        try:
            next_button = driver.find_element(By.XPATH, '//*[@id="l-container"]/div[3]/div/div/div/div[3]/button')
            next_button.click()
            time.sleep(DELAY)
            page += 1
        except ElementClickInterceptedException:
            break

    driver.close()

    # Create a dictionary with scrapped data.
    property_dict = {}

    for n in range(len(list_properties_address)):
        try:
            property_dict[n] = {
                "address": list_properties_address[n],
                "type": list_properties_info[n].split("\n")[0],
                "rooms": int(list_properties_info[n].split("\n")[1]),
                "baths": int(list_properties_info[n].split("\n")[2]),
                "link": list_properties_link[n],
                "price(£)": list_properties_price[n],
            }
        except IndexError:
            pass

    # Create dataframe from dictionary
    df = pd.DataFrame(property_dict).transpose().drop_duplicates()
    # print(df)
    # Export CSV
    df.to_csv(r"C:\Users\tmico\Desktop\clapham_houses.csv", index=False)

    break

os.startfile("C:/Users/tmico/Desktop/clapham_houses.csv")
