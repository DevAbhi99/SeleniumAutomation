from selenium.webdriver.common.by import By
from Locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver=driver

    def usernameElement(self):
        Username_element=self.driver.find_element(By.XPATH, Locators.username_xpath)
        return Username_element
    
    def passwordElement(self):
        Password_element=self.driver.find_element(By.XPATH, Locators.password_xpath)
        return Password_element
    
    def loginElement(self):
        Login_element=self.driver.find_element(By.XPATH, Locators.loginBtn_xpath)
        return Login_element
    

class MainPage:
    def __init__(self, driver):
        self.driver=driver
    
    def adminTab(self):
        Admin_element=self.driver.find_element(By.XPATH, Locators.Admin_xpath)
        return Admin_element
    
    def jobsTab(self):
        Jobs_element=self.driver.find_element(By.XPATH, Locators.Job_xpath)
        return Jobs_element
    
    def jobsTitle(self):
        Jobtitle_element=self.driver.find_element(By.XPATH, Locators.Jobtitles_xpath)
        return Jobtitle_element
    

class LogoutPage:
    def __init__(self, driver):
        self.driver=driver

    def profileTab(self):
        Profile_element=self.driver.find_element(By.XPATH, Locators.Profiletab_xpath)
        return Profile_element
    
    def logoutBtn(self):
        Logoutbtn_element=self.driver.find_element(By.XPATH, Locators.Logoutbtn_xpath)
        return Logoutbtn_element
    



    
    
