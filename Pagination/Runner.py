from Main import Main


class Runner:
    def __init__(self):
        self.main=Main()

    
    def run(self):
        self.main.login()

        self.main.mainPage()

        self.main.logoutPage()



obj=Runner()

obj.run()
        

