from BaseUtilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def loginSP(self):
        self.adddata_id("idToken1", "vaibhavtestsp")
        self.adddata_xpath("//input[@type = \'password\']", "Prime109")
        self.click_id("loginButton_0")
        home_page = HomePage(self.driver)
        return home_page



