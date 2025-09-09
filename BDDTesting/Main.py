from Elements import Elements

class Main:
    def __init__(self,driver):
        self.driver=driver
        self.element=Elements(driver)

    #Login page
    def usernameFill(self, username):
        self.element.usernameElement().send_keys(username)

    def passwordFill(self, password):
        self.element.passwordElement().send_keys(password)

    def loginClick(self):
        self.element.loginElement().click()

    #Main page
    def adminClick(self):
        self.element.adminElement().click()

    def jobClick(self):
        self.element.jobElement().click()

    def jobtitlesClick(self):
        self.element.jobtitlesElement().click()

    #logout page

    def profileClick(self):
        self.element.profileElement().click()

    def logoutClick(self):
        self.element.logoutElement().click()

    
    
        
