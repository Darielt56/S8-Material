from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
# We replace with our own URL
driver.get("https://cnt-2ec4dbdb-55d3-4c1d-aed2-17b8cb430e1a.containerhub.tripleten-services.com/")

# Give the page time to load
time.sleep(2)

#Enter the from address
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Pause for a second (to view the result)
time.sleep(1)

# Enter the to address
driver.find_element(By.ID, "to").send_keys("1300 1st St")

# Pause for a second (to view the result)
time.sleep(1)

# Quit the app
driver.quit()