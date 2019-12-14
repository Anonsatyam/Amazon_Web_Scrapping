from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import re
import time

path = (r"C:\Users\Satyam Singh\Downloads\geckodriver-v0.26.0-win64")

class AmazonBot(object):
    def __init__(self, iteams):

        self.amazon_url = "https://www.amazon.in/"
        self.iteams = iteams
        

        self.profile = webdriver.FirefoxProfile(path)
        self.options = Options()
        self.driver = webdriver.Firefox(firefox_profile=self.profile, firefox_options=self.options)

        self.driver.get(self.amazon_url)
    def search_iteams(self):
        urls = []
        prices = []
        names = []
        for iteam in self.iteams:
            print(f"searching for {iteam}")
            
            self.driver.get(self.amazon_url)

            search_input = self.driver.find_element_by_id('twotabsearchtextbox')
            search_input.send_keys(iteam)

            time.sleep(3)

            search_button = self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
            search_button.click()

iteams = ["samsung mobiles under 15000"]
amazon_bot = AmazonBot(iteams)
amazon_bot.search_iteams()




