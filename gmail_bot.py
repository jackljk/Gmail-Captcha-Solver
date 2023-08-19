from anticaptchaofficial.recaptchav2proxyless import *
from anticaptchaofficial.imagecaptcha import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import undetected_chromedriver 

import os

API_KEY = "808a06a109a5e91d1736b9c82777d433"
EMAIL = 'sndbbzz99@gmail.com'
PW = 'aass1122'


options = Options()
ua = UserAgent()
user_agent = ua.random
print(user_agent)

options.add_argument(f'--user-agent={user_agent}')
options.add_argument('--headless')
driver = webdriver.Chrome()

url = "https://mail.google.com"
page = driver.get(url)


#######################
# 1. Enter email
#######################
# Entering the email address
email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')

# Type text into the input field using send_keys()
email_input.send_keys(EMAIL)

#######################
# 2. Click Next
#######################
# Clicking the Next button
next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()

# Wait for the page to load
time.sleep(10)

#######################
# 3. Captcha for Recapcha
#######################
sitekey = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]').get_attribute('outerHTML')
sitekey_clean = sitekey.split('data-site-key="')[1].split('"><div class="eEgeR">')[0]
print(sitekey_clean)

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(API_KEY)
solver.set_website_url(url)
solver.set_website_key(sitekey_clean)

g_response = solver.solve_and_return_solution()

if g_response!= 0:
    print("g_response"+g_response)
else:
    print("task finished with error"+solver.error_code)

test = 'test'
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
time.sleep(5)
# token_box = driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response"]')
# token_box.send_keys(g_response)

driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "'+g_response+'";')

time.sleep(5)
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
#######################
# 3. Captcha for Image to text
#######################

# imgurl = driver.find_element(By.XPATH, '//*[@id="captchaimg"]').get_attribute('outerHTML')
# imgurl_clean = imgurl.split('src="')[1].split('" data-iml=')[0]
# print(imgurl_clean)

# solver = imagecaptcha()
# solver.set_verbose(1)
# solver.set_key(API_KEY)

# captcha_text = solver.solve_and_return_solution("https://accounts.google.com" + imgurl_clean)
# if captcha_text != 0:
#     print ("captcha text "+captcha_text)
# else:
#     print ("task finished with error "+solver.error_code)

    
# textbox = driver.find_element(By.XPATH, '//*[@id="captchainput"]')
# textbox.send_keys(captcha_text)

# next_captcha = driver.find_element(By.XPATH, '//*[@id="recaptchaNext"]/div/button')
# next_captcha.click()

time.sleep(1000)
#######################
# 4. Enter password
#######################
# Wait for the page to load
# time.sleep(10)

# # Entering the password
# password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
# password_input.send_keys(PW)

# # Clicking the Next button
# next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')

time.sleep(300)

driver.quit()

