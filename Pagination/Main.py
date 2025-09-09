from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Pages import LoginPage, MainPage, LogoutPage
import time

#To bypass firewalls and vpns

opts = webdriver.ChromeOptions()
opts.add_argument("--proxy-server='direct://'")
opts.add_argument("--proxy-bypass-list=*")
opts.add_argument("--disable-quic")
# Accept intercepted/self-signed certs if present
opts.set_capability("acceptInsecureCerts", True)

#Setting up drivers
service=Service(executable_path="chromedriver.exe")

driver=webdriver.Chrome(service=service,options=opts)

url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

class Main():
    def __init__(self):
        self.loginpage=LoginPage(driver)
        self.mainpage=MainPage(driver)
        self.logoutpage=LogoutPage(driver)


    def login(self):

        driver.get(url)

        driver.maximize_window()

        driver.implicitly_wait(10)

        self.loginpage.usernameElement().send_keys('Admin')

        time.sleep(3)

        self.loginpage.passwordElement().send_keys('admin123')
        
        time.sleep(3)

        self.loginpage.loginElement().click()

        time.sleep(3)

    def mainPage(self):
        driver.implicitly_wait(10)

        self.mainpage.adminTab().click()

        time.sleep(3)

        self.mainpage.jobsTab().click()

        time.sleep(3)

        self.mainpage.jobsTitle().click()

        driver.execute_script('window.scrollBy(0,200);')

        time.sleep(3)

        driver.save_screenshot('screenshot.png')

        time.sleep(3)

    
    def logoutPage(self):
        driver.implicitly_wait(10)

        self.logoutpage.profileTab().click()

        time.sleep(3)

        self.logoutpage.logoutBtn().click()

        time.sleep(3)


    def close(self):
        driver.implicitly_wait(10)

        driver.close()
        



