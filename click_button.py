import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(" https://cnt-decc392f-a59f-4efb-8f23-50bb60caa771.containerhub.tripleten-services.com/ ")

# make the app wait 2 seconds to give time for the page to load
time.sleep(2)

driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

time.sleep(2)

driver.quit()