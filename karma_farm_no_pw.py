bot_url = '' #your nubot dm URL
username = '' #flatironschool.com email username (without @flatironschool.com)
password = '' #flatironschool.com email password
spam_string = '' #the message to spam
iterations = 100 #how many times to spam it

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('./chromedriver')
#load page
driver.get(bot_url)
#login
driver.find_element_by_id("index_google_sign_in_with_google").click()
time.sleep(1)
login_form = driver.find_element_by_id("identifierId")
login_form.send_keys(username)
login_form.send_keys(Keys.ENTER)
time.sleep(1)
#enter password
password_form = driver.find_element_by_name('password')
password_form.send_keys(password)
password_form.send_keys(Keys.ENTER)
time.sleep(3)
#slack is open now. initialize action sequence and start spamming.
driver.find_element_by_id('msg_input').find_element_by_class_name('ql-editor').click()
actions = ActionChains(driver)
actions.send_keys(spam_string)
actions.send_keys(Keys.ENTER)
for i in range(iterations):
    actions.perform()
