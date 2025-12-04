import time
import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver


@pytest.mark.usefixtures("loginandlogoutsetup")
class BaseClass:

    def verify_element_presence(self,idtype, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((idtype, text)))

    def verify_element_clickable(self,idtype, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((idtype, text)))

    def sroll_to_bottom(self,idtype,text):
        try:
            self.driver.execute_script("window.scrollyBY(0,document.body.scrollheight")
        except:
            print("Unable to scroll to the Bottom...")

    def wait_for_sometime(self):
        time.sleep(2)


    def wait_ten_second(self):
        time.sleep(10)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
