from utilities.BaseClass import BaseClass

from pom.LoginPage import LoginPage

from pom.Logout import Logout
from pom.InvalidLoginPage import InvalidLoginPage


class Test_Invalid_LoginPage_Test(BaseClass):

    def test_verify_Invalid_loginPage(self):
        log = self.getLogger()
        log.info("Task Scrip Statrted")
        loginpage = LoginPage(self.driver)
        loginpage.setusername("admin123")
        loginpage.setpassword("12345")
        self.wait_for_sometime()
        loginpage.clickonloginbutton()

        invalidLogPage = InvalidLoginPage(self.driver)
        log.info("10 second wait")
        self.wait_ten_second()
        invalidLogPage.verify_error_msg()
        log.info("Error message validated successfully..")

