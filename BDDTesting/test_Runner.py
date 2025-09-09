from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Main import Main
from pytest_bdd import scenarios, given, when, then, parsers
import time
import pytest

scenarios('../BDDTesting/features/test.feature')

#By pass proxy and firewalls

opts = webdriver.ChromeOptions()
opts.add_argument("--proxy-server='direct://'")
opts.add_argument("--proxy-bypass-list=*")
opts.add_argument("--disable-quic")
# Accept intercepted/self-signed certs if present
opts.set_capability("acceptInsecureCerts", True)

#setting up google driver
service=Service(executable_path="chromedriver.exe")

driver=webdriver.Chrome(service=service, options=opts)

#url of the website
url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'


#Instantiating main class

obj=Main(driver)


#Login page automation
@given('The user is on the login page')
def openingLogin():
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

@when(parsers.parse('the user provides correct username "{username}" and password "{password}"'))
def loginDetails(username, password):
    obj.usernameFill(username)
    time.sleep(3)
    obj.passwordFill(password)
    time.sleep(3)

@when('The user clicks on the login button')
def login():
    obj.loginClick()
    time.sleep(3)

@then('The user go to the Orange HRM main page')
def mainPage():
    print('User is on the main page of Orange hrm')


#main page automation
@given('When the user is on the main page')
def mainPageStay():
    driver.implicitly_wait(10)
    print('User waits for the page to load')

@when('the user clicks on Admins tab')
def adminTab():
    obj.adminClick()
    time.sleep(3)

@when('The user clicks on Jobs tab and then Jobs title tab')
def jobsTab():
    obj.jobClick()
    time.sleep(3)
    obj.jobtitlesClick()
    time.sleep(3)

@then('The jobs are displayed and a screenshot is taken')
def screenshot():
    driver.execute_script('window.scrollBy(0,200);')
    time.sleep(2)
    driver.save_screenshot('Jobs.png')
    time.sleep(3)

#Logout page
@given('The user is on the main page')
def logoutMainPage():
    print('The user is still on main page')

@when('The user clicks on profile tab and dropdown icon')
def profile():
    obj.profileClick()
    time.sleep(3)

@when('The user clicks on the logout button')
def logout():
    obj.logoutClick()
    time.sleep(3)

@then('The user is logged out')
def exit():
    driver.quit()









