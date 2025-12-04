from utilities.BaseClass import BaseClass

from pom.LoginPage import LoginPage

from pom.Logout import Logout


class Test_Logout_Test(BaseClass):

    def test_verify_logout(self):
        loginpage = LoginPage(self.driver)
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.wait_for_sometime()
        loginpage.clickonloginbutton()

        logout = Logout(self.driver)
        self.wait_for_sometime()
        logout.clickonlogoutbutton()

