from ssl import Options
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from selenium.webdriver.chrome.options import Options

class PriceTracker:

    def get_price(product_name):
        
        options = Options()
        #options.headless  = True
        driver = webdriver.Chrome(executable_path='C:\R A J A S\Learn\Selenium\chromedriver.exe',chrome_options=options)
        driver.get('https://www.amazon.in/ref=nav_logo')
        #login_button = driver.find_element(By.CSS_SELECTOR,"span[id='nav-link-accountList-nav-line-1']")
        login_button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"span[id='nav-link-accountList-nav-line-1']"))
            )
        driver.maximize_window()
        login_button.click()

        phone_no = driver.find_element(By.CSS_SELECTOR,"input[type='email']")
        phone_no.send_keys('9892232364')
        driver.find_element(By.CSS_SELECTOR,"input[id='continue']").click()

        pswd = driver.find_element(By.CSS_SELECTOR,"input[type='password']")
        pswd.send_keys('harshit22')
        driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
        driver.find_element(By.CSS_SELECTOR,"input[id='signInSubmit']").click()

        search = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
        search.send_keys(product_name)
        driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
        
        products = driver.find_elements(By.CSS_SELECTOR,"h2[class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']")
        #my_product = products[1]
        #print(my_product)
        #for product in products:
        #product_name = products[0].text
        #    break
        my_product = driver.find_element(By.PARTIAL_LINK_TEXT,"Fitness Mantra® Y").text
        driver.find_element(By.PARTIAL_LINK_TEXT,"Fitness Mantra® Y").click()
        #my_product.click()
        time.sleep(2)
        
        #driver.current_window_handle
        windows = driver.window_handles[1]
        driver.switch_to_window(windows)

        time.sleep(2)
        price = driver.find_element(By.CSS_SELECTOR,"span[id*='priceblock']")
        price = price.text
        price1 = price[1::].replace(",","")

        #title = driver.find_element(By.CSS_SELECTOR,"span[id='productTitle']")
        #title = title.text
        #title.encode('utf-8')

        if float(price1) < 75000:

            sender_email = "rajextc225@gmail.com"
            rec_email = "pkatrale@gmail.com"
            password = "ikvtvnfaavvqrmtb"
            message = "Price Today is " + price1

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls() 
            server.login(sender_email,password)
            print("login sucess!")

            server.sendmail(sender_email,rec_email,message)
            print("email has been sent to receiver email")

        else:
            pass
        driver.quit()

  
p1 = PriceTracker
product_name = 'yoga mat'
p1.get_price(product_name)

    

