import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service('C:\\Users\\User\\PycharmProjects\\resource\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# go to the tested site
url = 'https://uch-market.ru/'
driver.get(url)
driver.maximize_window()

# click on the authorization_registration button
authorization_registration_button = driver.find_element(By.XPATH, '//i[@class="fa fa-check"]')
authorization_registration_button.click()

# fill in the authorization fields
mail = driver.find_element(By.XPATH, '//input[@name="email"]')
mail.send_keys('example_1@mail.ru')

password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys('*****')
time.sleep(2)

button_entrance = driver.find_element(By.XPATH, '//input[@value="Войти"]')
button_entrance.click()

# authorization confirmation
confirmation = driver.find_element(By.CSS_SELECTOR, '#content > h1')
assert confirmation.text == 'Подтверждение номера телефона'
print('authorization is confirmed')
