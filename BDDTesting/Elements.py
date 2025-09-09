from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators import Locators

class Elements:
    def __init__(self,driver):
        self.driver=driver

    #Login page    
    def usernameElement(self):
        username=self.driver.find_element(By.XPATH, Locators.UserName_xpath)
        return username
    
    def passwordElement(self):
        password=self.driver.find_element(By.XPATH, Locators.Password_xpath)
        return password
    
    def loginElement(self):
        login=self.driver.find_element(By.XPATH, Locators.Loginbtn_xpath)
        return login
    
    #Main page
    def adminElement(self):
        admin=self.driver.find_element(By.XPATH, Locators.Admin_xpath)
        return admin
    
    def jobElement(self):
        job=self.driver.find_element(By.XPATH, Locators.Job_xpath)
        return job

    def jobtitlesElement(self):
        jobtitles=self.driver.find_element(By.XPATH, Locators.Jobtitles_xpath)
        return jobtitles

    #Logout page
    def profileElement(self):
        profile=self.driver.find_element(By.XPATH, Locators.Profile_xpath)
        return profile

    def logoutElement(self):
        logout=self.driver.find_element(By.XPATH, Locators.Logoutbtn_xpath)
        return logout

    
        