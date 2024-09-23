from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
import time
from numpy import random
import pandas as pd

columns = ["Price", "Category", "Beds", "Baths", "Area", "Plot_size", "Address", "Broker","URL"]


def main():

    
    all_properties = []
    
    # Page browsing
    for page_id in range(1,207):
        start_time = time.time()
        url = f"https://www.realtor.com/realestateandhomes-search/Florida/pg-{page_id}"
        driver=webdriver.Firefox()
        driver.implicitly_wait(0.5)
        driver.get(url)
        random_time=random.randint(3,6)

        print(f"Waiting for: {random_time}s")
        time.sleep(random_time)

        # ---------------------Auto Scroll Down----------------------

        # Get the height of the page

        
        scroll_height = driver.execute_script("return document.body.scrollHeight") - 1000

        for i in range(0, scroll_height, 400):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.5)

        # ------------------------------------------------------------
        print(f"Scraping page: {page_id}")


        properties = driver.find_elements(By.XPATH, "//div[@class='BasePropertyCard_propertyCardWrap__30VCU']")
        
        for property in properties:

            property_data={}

            # Scraping 'Price'
            try:
                property_data['Price'] = property.find_element(By.XPATH, ".//div[@data-testid='card-price']//span").text
            except NoSuchElementException:
                property_data['Price'] = None  # Assign null value if element not found

            # Scraping 'Category'
            try:
                property_data['Category'] = property.find_element(By.XPATH, ".//div[@class='base__StyledType-rui__sc-108xfm0-0 hRTvWe message']").text
            except NoSuchElementException:
                property_data['Category'] = None

            # Scraping 'Beds'
            try:
                property_data['Beds'] = property.find_element(By.XPATH, ".//li[@data-testid='property-meta-beds']//span[@data-testid='meta-value']").text
            except NoSuchElementException:
                property_data['Beds'] = None

            # Scraping 'Baths'
            try:
                property_data['Baths'] = property.find_element(By.XPATH, ".//li[@data-testid='property-meta-baths']//span[@data-testid='meta-value']").text
            except NoSuchElementException:
                property_data['Baths'] = None

            # Scraping 'Area'
            try:
                property_data['Area'] = property.find_element(By.XPATH, ".//li[@data-testid='property-meta-sqft']").text
            except NoSuchElementException:
                property_data['Area'] = None

            # Scraping 'Plot Size'
            try:
                property_data['Plot_size'] = property.find_element(By.XPATH, ".//li[@data-testid='property-meta-lot-size']").text
            except NoSuchElementException:
                property_data['Plot_size'] = None

            # Scraping 'Address'
            try:
                address_part1 = property.find_element(By.XPATH, ".//div[@data-testid='card-address-1']").text
                address_part2 = property.find_element(By.XPATH, ".//div[@data-testid='card-address-2']").text
                property_data['Address'] = f"{address_part1}, {address_part2}"
            except NoSuchElementException:
                property_data['Address'] = None


            # Scraping 'Broker'
            try:
                property_data['Broker'] = property.find_element(By.XPATH, ".//div[@data-testid='broker-title']/span").text
            except NoSuchElementException:
                property_data['Broker'] = None

            # Scraping URL
            try:
                property_data['URL'] = property.find_element(By.XPATH, ".//a[contains(@href, 'realestateandhomes-detail')]").get_attribute("href")
            except NoSuchElementException:
                property_data['URL'] = None


            # Append the scraped data to the list
            all_properties.append(property_data)

        time.sleep(random.randint(0,3))
        driver.quit()
        end_time = time.time()
        print(f"Elapsed time for page {page_id}: {end_time-start_time}")

    # print(all_properties)

    df =  pd.DataFrame(data=all_properties, columns=columns)
    df.to_csv("data/property.csv", index=False)

    return


if __name__=="__main__":
    main()