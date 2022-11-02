from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:\\Users\\ZEPHYRUS\\Desktop\\Aplikacje\\Development\\chromedriver.exe")
browser = webdriver.Chrome(service=chrome_driver_path)

URL = "https://www.python.org/"
browser.get(URL)
upcoming_events = browser.find_element(By.CSS_SELECTOR, ".event-widget > div:nth-child(1) > ul:nth-child(3)")
list_of_dates = upcoming_events.text.split("[0-9]{4}-[0-9]{2}-[0-9]{2}")[0].split("\n")
dict_of_dates = {int((i + 1) / 2): {"time": list_of_dates[i], "name": list_of_dates[i + 1]} for i in
                 range(0, len(list_of_dates), 2)}
print(dict_of_dates)
# driver.close()
browser.quit()
