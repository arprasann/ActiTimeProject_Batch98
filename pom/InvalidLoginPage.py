from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

class InvalidLoginPage(BaseClass):

    errormsg = (By.XPATH,"(//span[@class='errormsg'])[1]")

    def __init__(self,driver):
        self.driver = driver


    def verify_error_msg(self):
        self.verify_element_presence(By.XPATH,"(//span[@class='errormsg'])[1]")
        error = self.driver.find_element(*InvalidLoginPage.errormsg)
        self.wait_for_sometime()
        if error.is_displayed():
            if error.text == "Username or Password is invalid. Please try again.":
                print("True: It is Inavlaid LoginPage ")
        else:
            print("False: It is not a Invalid LoginPage ")
