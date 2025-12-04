from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass

class Reports(BaseClass):

    report = (By.XPATH,"//div[text()='REPORTS']")

    newReport = (By.XPATH,"//span[text()='New Report']")

    configurereport = (By.ID,"configureReportParametersButton")

    generatereport = (By.XPATH,"(//span[text()='Generate HTML Report'])[2]")

    exportcsvreport = (By.XPATH, "//td[contains(text(),'Export to CSV')]")

    def __init__(self,driver):
        self.driver = driver

    def clcikonreport(self):
        self.verify_element_clickable(By.XPATH,"//div[text()='REPORTS']")
        return self.driver.find_element(*Reports.report).click()

    def clcikonNewreport(self):
        self.verify_element_clickable(By.XPATH,"//span[text()='New Report']")
        return self.driver.find_element(*Reports.newReport).click()

    def clcikonconfigurereport(self):
        self.verify_element_clickable(By.ID,"configureReportParametersButton")
        return self.driver.find_element(*Reports.configurereport).click()

    def clcikongeneratereport(self):
        self.verify_element_clickable(By.XPATH,"(//span[text()='Generate HTML Report'])[2]")
        return self.driver.find_element(*Reports.generatereport).click()

    def clcikonexportcsvreport(self):
        self.verify_element_clickable(By.XPATH, "//td[contains(text(),'Export to CSV')]")
        return self.driver.find_element(*Reports.exportcsvreport).click()
