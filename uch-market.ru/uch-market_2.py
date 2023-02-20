import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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

# fill in the required fields
mail = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_email"]')))
mail.send_keys('example_1@mail.ru')

password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_password"]')))
password.send_keys('*****')

repeat_password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_confirm_password"]')))
repeat_password.send_keys('*****')

first_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_firstname"]')))
first_name.send_keys('Иван')

last_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_lastname"]')))
last_name.send_keys('Иванов')

phone_number = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_telephone"]')))
phone_number.send_keys('+7 111 111 11 11')
time.sleep(5)

region = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_zone_id"]')))
region.send_keys(Keys.ENTER)

choose_region = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_zone_id"]/option[17]')))
choose_region.click()

city = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_city"]')))
city.send_keys('Иваново')

index = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_postcode"]')))
index.send_keys('153000')

adress = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register_address_1"]')))
adress.send_keys(' ул. Ленина, дом 1')

continue_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="simpleregister_button_confirm"]')))
continue_button.click()
time.sleep(2)
print('this user already exists go to the authorization page')

# go to the page of already registered users
action = ActionChains(driver)
confirm_registration = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#simpleregister > p > a')))
action.move_to_element(confirm_registration).perform()
confirm_registration.click()

# we enter the data of the registered user
confirm_mail = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]')))
confirm_mail.send_keys('example_1@mail.ru')

confirm_password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
confirm_password.send_keys('*****')
time.sleep(2)

button_entrance = driver.find_element(By.XPATH, '//input[@value="Войти"]')
button_entrance.click()

# authorization confirmation
confirmation = driver.find_element(By.CSS_SELECTOR, '#content > h1')
assert confirmation.text == 'Подтверждение номера телефона'
print('authorization is confirmed')
print('the test is passed, you cannot re-register with an existing user')
