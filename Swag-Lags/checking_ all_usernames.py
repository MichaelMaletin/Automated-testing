from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
s = Service('C:\\Users\\User\\PycharmProjects\\resource\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

class Verify_username():

    def __init__(self, driver):
        self.driver = driver

    def authorisation(self, login, password):
#authorisation#
        username_input = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        username_input.send_keys(login)

        password_input = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        login_button.click()
        print('entrance')
#back to new  authorisation#
        menu_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
        menu_button.click()

        logout = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        logout.click()
        print("exit")

class Login():

    def enumeration_users(self):
        url = 'https://www.saucedemo.com/'
        driver.get(url)
        driver.maximize_window()
        print("welcome")
#list usernames#
        usernames = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        password = 'secret_sauce'
# enumeration users for authorisation#
        item = 0
        while item < len(usernames):
            login = usernames[item]
#catching exceptions#
            try:
                page_authorisation = Verify_username(driver)
                page_authorisation.authorisation(login, password)
            except TimeoutException:
                print('exception')
                driver.refresh()
            item += 1
#launching#
test = Login()
test.enumeration_users()
