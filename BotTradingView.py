from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import org.openga.selenium.support.ui.select

driver= webdriver.Chrome('C:/Users/Alejandro/Documents/Programas/WebdriverChrome/chromedriver_win32/chromedriver.exe')
driver.get('https://es.tradingview.com/')

time.sleep(15)

# driver.send_keys(Keys.TAB)
# user= driver.find_element(By.NAME, "username")
# password= driver.find_element(By.NAME, 'password')

# user.send_keys('alejandro')
# password.send_keys('123')
# password.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()
