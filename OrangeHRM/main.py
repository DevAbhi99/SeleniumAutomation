#Import package
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Setup chrome driver
service=Service(executable_path="chromedriver.exe")


opts = webdriver.ChromeOptions()
opts.add_argument("--proxy-server='direct://'")
opts.add_argument("--proxy-bypass-list=*")
opts.add_argument("--disable-quic")
# Accept intercepted/self-signed certs if present
opts.set_capability("acceptInsecureCerts", True)


driver=webdriver.Chrome(service=service, options=opts)


url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

#Code
driver.implicitly_wait(10)  #Wait until all the the page is loaded properly

driver.get(url)


#Test scripts

username=driver.find_element(By.NAME, 'username')

username.send_keys('Admin')

time.sleep(3)

password=driver.find_element(By.NAME, 'password')

password.send_keys('admin123')

time.sleep(3)

button=driver.find_element(By.XPATH, '//button[text()=" Login "]')

button.click()

time.sleep(30)

#Next page

driver.implicitly_wait(10) #Wait for the page to load

admin=driver.find_element(By.XPATH, '//span[text()="Admin"]')

admin.click()

time.sleep(3)

job=driver.find_element(By.XPATH, '//span[text()="Job "]')

job.click()

time.sleep(3)

jobTitles=driver.find_element(By.XPATH, '//a[text()="Job Titles"]')

jobTitles.click()

time.sleep(3)


#Scroll down 

driver.execute_script('window.scrollBy(0,200);')

#take screenshot

driver.save_screenshot('screenshot.png')

driver.quit()







