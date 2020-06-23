
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


chrome_path = r'/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.maximize_window()
# original site
driver.get("https://agileengine.bitbucket.io/beKIvpUlPMtzhfAy/samples/sample-0-origin.html")

# finding an element with its class name (success)
wait = WebDriverWait(driver, 10)
okay_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn btn-success")))
print(okay_button.text)

driver.close()
