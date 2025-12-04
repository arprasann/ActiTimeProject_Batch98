from utilities.BaseClass import BaseClass

from pom.LoginPage import LoginPage
from pom.Logout import Logout
from pom.Reports import Reports
from pom.Users import Create_Users


class Test_Verify_Export_CSV_Reports(BaseClass):

    def test_verify_reports(self):
        loginpage = LoginPage(self.driver)
        self.wait_for_sometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.wait_for_sometime()
        loginpage.clickonloginbutton()
        self.wait_for_sometime()

        u1 = Create_Users(self.driver)
        self.wait_for_sometime()
        u1.click_On_Users()
        self.wait_for_sometime()
        u1.click_On_add_User()
        self.wait_for_sometime()
        u1.set_first_name("Dinga")
        u1.set_last_name("Manga")
        u1.set_email("Dingamanaga345@gmail.com")
        self.wait_for_sometime()
        u1.click_on_Create_User_Button()
        u1.set_user_name("admin1234")
        u1.set_password("Dinga1234")
        u1.set_reenter_password("Dinga1234")

        logout = Logout(self.driver)
        self.wait_for_sometime()
        logout.clickonlogoutbutton()
        self.wait_for_sometime()
