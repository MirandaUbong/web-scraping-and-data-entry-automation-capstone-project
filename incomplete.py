from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)


# ZWILLO (RAN INTO ROBOT ISSUES)

# driver.get("https://www.zillow.com/hampshire-il/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-88.6040332719515%2C%22east%22%3A-88.24011115281087%2C%22south%22%3A42.05807889717635%2C%22north%22%3A42.29571424155386%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A52394%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D")

# all_links = driver.find_elements(By.CSS_SELECTOR, ".short-list-cards li a")
# for link in all_links:
#     print(link.text)


# SPARE ROOM

driver.get("https://www.spareroom.co.uk/flatshare/?search_id=1256159971&")
property_links = driver.find_elements(By.CSS_SELECTOR, ".order-2 li a")
# print(property_links)

links = []
for link in property_links:
    links.append(link.text)
    print(links)

# property_addresses = driver.find_elements(By.CSS_SELECTOR, ".order-2 li em span")
# addresses = []
# for address in property_addresses:
#     addresses.append(address.text)
#     print(addresses)
