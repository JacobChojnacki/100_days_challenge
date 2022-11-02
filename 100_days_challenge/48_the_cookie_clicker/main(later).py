from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def check_for_upgrade(upgrades, clicks):
    return_upgrade = None
    for upgrade in upgrades:
        if int(upgrades[upgrade]['price']) < clicks:
            return_upgrade = upgrades[upgrade]['ID']
    return return_upgrade


# Link to our game
URL = "http://orteil.dashnet.org/experiments/cookie/"

# --------------------------------- CHROME CONFIGURATION --------------------------- #
chrome_driver_path = Service("C:\\Users\\ZEPHYRUS\\Desktop\\Aplikacje\\Development\\chromedriver.exe")
browser = webdriver.Chrome(service=chrome_driver_path)
# ---------------------------------------------------------------------------------- #
browser.get(URL)
# ----------------------------------- GAME DATA ------------------------------------ #

money = browser.find_element(By.CSS_SELECTOR, "#money").text

if "," in money:
    money = money.replace(",", "")
cookie_count = int(money)

cookie = browser.find_element(By.CSS_SELECTOR, "#cookie")
grandma = browser.find_element(By.CSS_SELECTOR, "#buyGrandma")
portal = browser.find_element(By.CSS_SELECTOR, "#buyPortal")
alchemy = browser.find_element(By.CSS_SELECTOR, "#buyAlchemy\ lab")
shipment = browser.find_element(By.CSS_SELECTOR, "#buyShipment")
mine = browser.find_element(By.CSS_SELECTOR, "#buyMine")
factory = browser.find_element(By.CSS_SELECTOR, "#buyFactory")
selector = browser.find_element(By.CSS_SELECTOR, "#buyCursor")

while True:
    cookie.click()
