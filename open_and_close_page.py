from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver.get("SERVER URL")

# Check url contains tripleten-services.com
assert "tripleten-services.com" in driver.current_url

# Close the browser
driver.quit()