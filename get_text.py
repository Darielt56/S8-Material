import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" https://cnt-aeacb6fc-96f3-4441-b3d8-8368dbe85c12.containerhub.tripleten-services.com/ ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM field and fill it in
driver.find_element(By.ID,"from").send_keys("East 2nd Street, 601")

# Find the TO field and fill it in
driver.find_element(By.ID,"to").send_keys("1300 1st St")

time.sleep(2)

# Get the text from "Fastest" mode
mode = driver.find_element(By.XPATH,"//div[@class='mode active']").text

time.sleep(2)

# Assert that the text of the mode variable is "Fastest"
assert mode == "Fastest"

driver.quit()
