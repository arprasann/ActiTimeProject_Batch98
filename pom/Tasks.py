from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass

class Tasks(BaseClass):

    task = (By.XPATH,"//div[text()='TASKS']")
    filtertaskByName = (By.NAME,"visiableFilterString")
    applyFilter = (By.ID,"tasksFilterSubmitButton")

    def __init__(self,driver):
        self.driver = driver

    def clickonTask(self):
        self.verify_element_clickable(By.XPATH,"//div[text()='TASKS']")
        return self.driver.find_element(*Tasks.task).click()

    def sendtextfiltertaskbyName(self,text):
        return self.driver.find_element(*Tasks.filtertaskByName).send_keys(text)

    def clcikonapplyfilter(self):
        return self.driver.find_element(*Tasks.applyFilter).click()

