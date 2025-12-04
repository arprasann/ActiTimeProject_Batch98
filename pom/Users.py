import random

from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.BaseClass import BaseClass
from random import *

class Create_Users(BaseClass):

    users = (By.XPATH,"//div[text()='USERS']")
    user = (By.XPATH, "//div[text()='Add User']")
    firstname = (By.NAME, "firstName")
    lastname = (By.NAME, "lastName")
    email = (By.NAME, "email")
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    reenterpassword = (By.NAME, "passwordCopy")
    createUser = (By.XPATH,"//*[text()='Create User1']")


    def __init__(self,driver):
        self.driver = driver

    def click_On_Users(self):
        return self.driver.find_element(*Create_Users.users).click()



    def click_On_add_User(self):
        return self.driver.find_element(*Create_Users.user).click()

    def set_first_name(self,fn):
        return self.driver.find_element(*Create_Users.firstname).send_keys(fn)

    def set_last_name(self,ln):
        return self.driver.find_element(*Create_Users.lastname).send_keys(ln)

    def set_email(self,email1):
        return self.driver.find_element(*Create_Users.email).send_keys(email1)

    def set_user_name(self,un):
        return self.driver.find_element(*Create_Users.username).send_keys(un)

    def set_password(self,pw):
        return self.driver.find_element(*Create_Users.password).send_keys(pw)

    def set_reenter_password(self,rpw):
        return self.driver.find_element(*Create_Users.reenterpassword).send_keys(rpw)

    def click_on_Create_User_Button(self):
        return  self.driver.find_element(*Create_Users.createUser).click()