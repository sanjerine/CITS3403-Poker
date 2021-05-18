import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#get path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

#create new chrom session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

#navigate to register
driver.get("http://127.0.0.1:5000/register")

#enter details
search_field = driver.find_element_by_name("username")
search_field.send_keys("qwerty")
search_field = driver.find_element_by_name("email")
search_field.send_keys("qwerty@gmail.com")
search_field = driver.find_element_by_name("password")
search_field.send_keys("qwerty")
search_field = driver.find_element_by_name("repeatpassword")
search_field.send_keys("qwerty")

search_field = driver.find_element_by_name("submit").click()

# got to login page same as before (but login)

driver.get("http://127.0.0.1:5000/login")

search_field = driver.find_element_by_name("username")
search_field.send_keys("qwerty")

search_field = driver.find_element_by_name("password")
search_field.send_keys("qwerty")

search_field = driver.find_element_by_name("submit").click()

#go through quiz
driver.get("http://127.0.0.1:5000/quiz")

driver.find_element_by_id("{{answer.id}}").click()

driver.get("/logout")

driver.quit()

