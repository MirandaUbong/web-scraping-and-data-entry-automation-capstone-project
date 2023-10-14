from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

zillow_url = "https://www.zillow.com/chicago-il/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A42.185798941212674%2C%22south%22%3A41.94979298126408%2C%22east%22%3A-88.2160484897461%2C%22west%22%3A-88.83196951025391%7D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A17426%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A11%7D"
response = requests.get(zillow_url, headers=header)

# print(response)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.title)

addresses = [addr.get_text().split(" | ")[-1] for addr in soup.select("[data-test='property-card-addr']")]
print(addresses)

prices = [pri.get_text() for pri in soup.select("[data-test='property-card-price']")]
print(prices)

links = [lk.get_text() for lk in soup.select("[data-test='.property-card-link']")]
print(links)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

google_form_link = "MY FORM"

for n in addresses:
    driver.get(google_form_link)

    time.sleep(2)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(addresses)
    price.send_keys(prices)
    link.send_keys(links)
    submit.click()
