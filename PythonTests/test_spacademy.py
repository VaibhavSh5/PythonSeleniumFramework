import time

import pytest

from BaseUtilities.BaseClass import BaseClass


class TestSpCases(BaseClass):
    @pytest.mark.skip
    def test_sptest(self):
        self.click_id('dashboard-toggle')
        self.click_id('watCommDir')
        self.click_id('watAddSupplier')
        self.click_linktext('Add Supplier')
        checkboxes = self.multiple_elements_xpath('//td[@class= \'widget\']/input[@type=\'checkbox\']')
        for items in checkboxes:
            items.click()

        assert self.driver.find_element_by_id('sensitiveTransactionSecurityId').is_selected()
        self.assertFalse(self.driver.find_element_by_id('createAdminUser').is_selected(), "The test case is not failed")
        time.sleep(5)
        print("Fixture tested!!")

    @pytest.mark.checkoutcart
    def test_checkoutcart(self):
        self.adddata_name("name", "Vaibhav Sharma QA Engineer")
        self.click_xpath("//a[contains(@href, \'shop\')]")
        expected_Text = self.driver.find_element_by_link_text('Blackberry').text
        self.click_xpath('//div[@class= \'card h-100\']//a[normalize-space()= '
                         '\'Blackberry\']/../../following-sibling::div[1]/button')
        self.click_xpath('//a[@class = \'nav-link btn btn-primary\']')
        assert expected_Text == self.driver.find_element_by_link_text('Blackberry').text

        self.click_xpath('//button[@class= \'btn btn-success\']')
        self.adddata_id("country", "Ind")

        suggestions = self.driver.find_elements_by_xpath('//div[@class= \'suggestions\']/ul/li/a')

        for items in suggestions:
            if items.text == 'India':
                items.click()
                break

        print("The test has passed successfully!!")
