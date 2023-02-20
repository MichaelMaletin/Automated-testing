import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
s = Service('C:\\Users\\User\\PycharmProjects\\resource\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# go to the tested site
url = 'https://uch-market.ru/'
driver.get(url)
driver.maximize_window()

# click on the authorization registration buttons
authorization_registration_button = driver.find_element(By.XPATH, '//i[@class="fa fa-check"]')
authorization_registration_button.click()

# new user
continue_registration_button = driver.find_element(By.XPATH, '//a[@class="btn btn-primary"]')
continue_registration_button.click()

# exploring the input fields
mail = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_email"]')))
mail.send_keys('1')
mail.send_keys(Keys.ENTER)
time.sleep(1)
mail.send_keys(Keys.BACKSPACE)
mail.send_keys('# $ % @ ++')
mail.send_keys(Keys.ENTER)
time.sleep(1)
mail.send_keys(Keys.BACKSPACE*10)
mail.send_keys('@')
mail.send_keys(Keys.ENTER)
time.sleep(1)
mail.send_keys(Keys.BACKSPACE)
mail.send_keys('@@@@@@@@@@@')
mail.send_keys(Keys.ENTER)
time.sleep(1)

password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_password"]')))
password.send_keys('***')
password.send_keys(Keys.ENTER)
password.send_keys(Keys.BACKSPACE*3)
password.send_keys('******')
password.send_keys(Keys.ENTER)

repeat_password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_confirm_password"]')))
repeat_password.send_keys('***')
repeat_password.send_keys(Keys.ENTER)
repeat_password.send_keys(Keys.BACKSPACE*3)
repeat_password.send_keys('******')
repeat_password.send_keys(Keys.ENTER)

first_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_firstname"]')))
first_name.send_keys('1+1=?')
time.sleep(1)
first_name.send_keys(Keys.BACKSPACE*5)
first_name.send_keys('◕-^-◕')

last_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_lastname"]')))
last_name.send_keys('(2+2)*2 == 2')

phone_number = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_telephone"]')))
phone_number.send_keys('+7')
phone_number.send_keys(Keys.ENTER)
time.sleep(1)
phone_number.send_keys(Keys.BACKSPACE*2)
phone_number.send_keys('grey with buttons')
phone_number.send_keys(Keys.ENTER)

city = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_city"]')))
city.send_keys('#')
city.send_keys(Keys.ENTER)
time.sleep(1)
city.send_keys('#')

index = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_postcode"]')))
index.send_keys('+')
index.send_keys(Keys.ENTER)
time.sleep(1)
index.send_keys('+')

adress = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_address_1"]')))
adress.send_keys('12')
adress.send_keys(Keys.ENTER)
time.sleep(1)
adress.send_keys(Keys.BACKSPACE*2)
adress.send_keys('???')
adress.send_keys(Keys.ENTER)
time.sleep(5)


