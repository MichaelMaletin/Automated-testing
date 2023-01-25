import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:\\pythonSelenium\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://www.saucedemo.com/'
driver.get(url)
login = 'standard_user'
password_main = 'secret_sauce'
driver.maximize_window()
#authorization#
user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys(login)
print('login entered')

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys(password_main)
print('password entered')

password.send_keys(Keys.ENTER)
time.sleep(2)
print('login button clicked')

#product#
product = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
title_product = product.text
print(title_product)

price_product = driver.find_element(By.XPATH, '//*[@class="inventory_item_price"]')
item_price = price_product.text
print(item_price)

select_product = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
select_product.click()
time.sleep(2)
print('select_product clicked')

#cart#
cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]')
cart.click()
print('entered cart')
time.sleep(2)

#check the price and title in cart#
product_cart = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
title_product_cart = product_cart.text
assert title_product_cart == title_product
print('product in cart equal')

price_cart = driver.find_element(By.XPATH, '//*[@class="inventory_item_price"]')
item_price_cart = price_cart.text
assert item_price_cart == item_price
print('price in cart equal')

checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
print('product and price checked in cart')
time.sleep(2)

#info about user#
first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys('Иван')
print('first_name: Иван')

last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys('Иванов')
print('last_name: Иванов')

postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
postal_code.send_keys('12345')
print('postal_code: 12345')

continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
continue_button.click()
print('continue button clicked')
time.sleep(2)

#order confirmation#
product_confirm = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
title_product_confirm = product_confirm.text
assert title_product_confirm == title_product
print('title_product_confirmed')

price_confirm = driver.find_element(By.XPATH, '//*[@class="inventory_item_price"]')
item_price_confirm = price_confirm.text
assert item_price_confirm == item_price
print('item_price_confirmed')

finish = driver.find_element(By.XPATH, '//*[@id="finish"]')
finish.click()
time.sleep(2)

#confirmation of sending the order#
dispatch = driver.find_element(By.XPATH, '//*[@class="complete-text"]')
item_dispatch = dispatch.text
assert item_dispatch == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
print('The test was successful!!!')




