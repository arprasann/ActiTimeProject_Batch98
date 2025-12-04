from utilities.BaseClass import BaseClass

from pom.LoginPage import LoginPage
from pom.Logout import Logout
from pom.Reports import Reports
from pom.CheckBox import CheckBox


class Test_Verify_CheckBox(BaseClass):

    def test_verify_checkbox(self):
        checkBox = CheckBox(self.driver)
        self.wait_for_sometime()
        checkBox.clickoncheckbox()
        self.wait_for_sometime()


