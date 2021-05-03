import time

import pytest

from BaseUtilities.BaseClass import BaseClass
from TestData.SupplierFormData import SupplierFormData


class AddSupplier(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def addsupplier(self):
        self.click_linktext('Add Supplier')
        checkboxes = self.multiple_elements_xpath('//td[@class= \'widget\']/input[@type=\'checkbox\']')
        for items in checkboxes:
            items.click()
