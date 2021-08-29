from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r"C:\R A J A S\Learn\Selenium\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element_by_id('nav-link-accountList').click()
driver.find_element_by_id('ap_email').send_keys('9892232364')
driver.find_element_by_id('continue').click()
driver.find_element_by_css_selector("input[type='password']").send_keys('harshit22')
driver.find_element_by_xpath("//input[@id='signInSubmit']").click()
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('IphoneX')
driver.find_element_by_id("nav-search-submit-button").click()
driver.execute_script('window.scrollTo(0,600)')

models = driver.find_elements_by_css_selector("span[class='a-size-medium a-color-base a-text-normal']")
for model in models:
    if model.text == 'New Apple iPhone XR (64GB) - (Product) RED':
        driver.find_element_by_link_text("New Apple iPhone XR (64GB) - (Product) RED").click()
        driver.find_element_by_id("add-to-cart-button").click()