from utilities.BaseClass import BaseClass
from pom.Logout import Logout
from pom.LoginPage import LoginPage
from pom.Tasks import Tasks

class Test_Verify_TaskName(BaseClass):

    def test_verify_tasks(self):
        log = self.getLogger()
        log.info("Task Scrip Statrted")
        loginpage = LoginPage(self.driver)
        self.wait_for_sometime()
        loginpage.setusername("admin")
        loginpage.setpassword("manager")
        self.wait_for_sometime()
        loginpage.clickonloginbutton()

        task = Tasks(self.driver)
        task.clickonTask()
        self.wait_for_sometime()
        log.info(task.sendtextfiltertaskbyName("MangaKonga1"))

        self.wait_for_sometime()
        task.clcikonapplyfilter()
        self.wait_for_sometime()

        logout = Logout(self.driver)
        self.wait_for_sometime()
        logout.clickonlogoutbutton()
        self.wait_for_sometime()
        log.info("Tasks scrip Executed Successfully..")