
from utilities.BaseClass import BaseClass
from pom.LoginPage import LoginPage

class Test_LoginPage(BaseClass):

    def test_loginpage(self):
        log = self.getLogger()

        log.info("Valid Login Page Script started...")
        loginpage = LoginPage(self.driver)
        self.wait_for_sometime()
        log.info("Enter the valid Username")
        loginpage.setusername("admin")

        log.info("Succssfully fetched data from dataload")
        self.wait_for_sometime()
        log.info("Enter The Valid Password")
        loginpage.setpassword("manager")
        self.wait_for_sometime()
        log.info("Click On Login Button")
        loginpage.clickonloginbutton()
        self.wait_for_sometime()
        log.info("Login Page scrip successfully Executed")
