from BaseUtilities.BaseClass import BaseClass
from PageObjects.AddSupplier import AddSupplier


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def homepage(self):
        self.click_id('dashboard-toggle')
        self.click_id('watCommDir')
        self.click_id('watAddSupplier')
        add_supplier = AddSupplier(self.driver)
        return add_supplier
