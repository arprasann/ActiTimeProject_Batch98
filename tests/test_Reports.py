from utilities.BaseClass import BaseClass

from pom.LoginPage import LoginPage
from pom.Logout import Logout
from pom.Reports import Reports


class Test_Verify_Export_CSV_Reports(BaseClass):

    def test_verify_reports(self):
        loginpage = LoginPage(self.driver)
        self.wait_for_sometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.wait_for_sometime()
        loginpage.clickonloginbutton()
        self.wait_for_sometime()

        reports = Reports(self.driver)
        self.wait_for_sometime()
        reports.clcikonreport()
        self.wait_for_sometime()
        reports.clcikonNewreport()
        self.wait_for_sometime()
        reports.clcikonconfigurereport()
        self.wait_for_sometime()
        reports.clcikongeneratereport()
        self.wait_for_sometime()
        reports.clcikonexportcsvreport()

        logout = Logout(self.driver)
        self.wait_for_sometime()
        logout.clickonlogoutbutton()
        self.wait_for_sometime()
