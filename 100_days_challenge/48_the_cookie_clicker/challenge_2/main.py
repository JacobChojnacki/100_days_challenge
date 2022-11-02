from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("C:\\Users\\ZEPHYRUS\\Desktop\\Aplikacje\\Development\\chromedriver.exe")
browser = webdriver.Chrome(service=chrome_driver_path)

URL = "http://secure-retreat-92358.herokuapp.com/"
browser.get(URL)

# find elements to sign up
fName = browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(3)")
lName = browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(4)")
email = browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(5)")

# send data
fName.send_keys("")
lName.send_keys("")
email.send_keys("")
email.send_keys(Keys.ENTER)
