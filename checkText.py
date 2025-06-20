from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
# Replace our link with your own server link here
driver.get("https://cnt-586207c5-cdde-488a-b988-01f263ab368a.containerhub.tripleten-services.com/")

time.sleep(2)

# Gets the element's text
disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Assert that the text of the discalimer variable is "PLATFORM"
assert disclaimer == "PLATFORM"
print(disclaimer)
driver.quit()