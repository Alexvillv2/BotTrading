#SERVICIO LOG IN

#LOG IN TRADING VIEW


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

user= "xxxxx"
pas="xxxx"

driver= webdriver.Chrome()
driver.get('https://es.tradingview.com/')
time.sleep(10)


driver.find_element(By.XPATH,'//*[@id="one-tap-signin-container"]').click()

#obj= driver.find_element(By.XPATH,'//*[@id="email-signin__user-name-input__a5b4d798-c74f-439d-95d1-a9167f5e7e02"]')
#obj.send_keys(user)
#obj= driver.find_element_by_xpath('//*[@id="email-signin__password-input__a5b4d798-c74f-439d-95d1-a9167f5e7e02"]')
#obj.send_keys(pas)

#driver.find_element_by_xpath('//*[@id="email-signin__submit-button__a5b4d798-c74f-439d-95d1-a9167f5e7e02"]/span[2]').click()

