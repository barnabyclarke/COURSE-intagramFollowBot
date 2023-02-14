# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time

EMAIL = "x"
PASSWORD = "x"
ACCOUNT = "cristiano"


class InstaFollower:

    def __init__(self):
        self.chrome_driver_path = Service("C:/Users/BC/Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/")

    def login(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/'
                       'button[2]')
        )).click()  # Accept cookies
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/'
                       'form/div/div[1]/div/label/input')
        )).send_keys(EMAIL)  # Enter email
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/'
                       'form/div/div[2]/div/label/input')
        )).send_keys(PASSWORD)  # Enter password
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/'
                       'form/div/div[3]/button/div')
        )).click()  # Click log in
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/'
                       'div/div/button')
        )).click()  # Don't save info
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/'
                       'div[3]/button[2]')
        )).click()  # No notifications

    def find_followers(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/'
                       'div[2]/div/a/div/div[2]/div/div')
        )).click()  # Go to Search
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/'
                       'div[2]/div[1]/div/input')
        )).send_keys(ACCOUNT)  # Input account
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/'
                       'div[2]/div[2]/div/div[1]/div/a/div')
        )).click()  # Click on account
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/'
                       'section/ul/li[2]/a/div/span')
        )).click()  # Click on account followers

    def follow(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/'
                       'div[1]/div/div[1]/h1/div')
        ))  # Waits until followers pop up appears
        # self.driver.refresh()
        account_list = self.driver.find_elements(
            By.CSS_SELECTOR, '._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm'
        )  # Gets all accounts shown
        # account_list = account.find_elements(By.XPATH, '/div[3]/button')
        for account in account_list:
            time.sleep(0.2)
            ActionChains(self.driver).scroll_to_element(account).perform()
            print(account.text)
            try:
                account.find_element(By.CSS_SELECTOR, 'button').click()
            except StaleElementReferenceException:
                account.find_element(By.CSS_SELECTOR, 'button').click()
