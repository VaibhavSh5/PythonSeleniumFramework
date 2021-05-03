import pathlib
import time
import os

import pytest

from BaseUtilities.BaseClass import BaseClass
from PageObjects.LoginPage import LoginPage
from TestData.SupplierFormData import SupplierFormData


class TestCases(BaseClass):

    def test_addsupplier(self):
        login_page = LoginPage(self.driver)
        home_page = login_page.loginSP()
        add_supplier = home_page.homepage()
        add_supplier.addsupplier()
        assert self.driver.find_element_by_id('sensitiveTransactionSecurityId').is_selected()
        # self.assertFalse(self.driver.find_element_by_id('createAdminUser').is_selected(), "The test case is not failed")
        # self.assertFalse(self.driver.find_element_by_id('sensitiveTransactionSecurityId').is_selected(), "The test case has failed here!!")
        time.sleep(5)
        print("Checkboxes are tested!!")

    @pytest.fixture(params=SupplierFormData.supplier_form_data)
    def getsupplierdata(self, request):
        return request.param

    def test_addsupplierwithdata(self, getsupplierdata):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        log.info("Login has been completed for SP User")
        home_page = login_page.loginSP()
        home_page.homepage()
        log.info("User is redirected to the Homepage!!")
        self.click_linktext('Add Supplier')
        log.info("Adds Supplier link is clicked from the menu")
        self.adddata_id("_companyName", getsupplierdata["CompanyName"])
        log.info("Company name has been added into the textbox!! --> " + getsupplierdata["CompanyName"])
        self.adddata_id("_tdLegalName", getsupplierdata["CompanyLegalName"])
        log.info("Company Legal Name has been added into the textbox!!" + getsupplierdata["CompanyLegalName"])
        self.adddata_id("_street1", getsupplierdata["Street1"])
        log.info("Street 1 has been added into the textbox!!" + getsupplierdata["Street1"])
        self.adddata_id("_street2", getsupplierdata["Street2"])
        log.info("Street 2 has been added into the textbox!!" + getsupplierdata["Street2"])
        self.adddata_id("_city", getsupplierdata["City"])
        log.info("City has been added into the textbox!!" + getsupplierdata["City"])

    @pytest.fixture(params=SupplierFormData.getsupplierdata())
    def getsupplierexceldata(self, request):
        return request.param

    def test_addsupplierwithexceldata(self, getsupplierexceldata):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        log.info("Login has been completed for SP User")
        home_page = login_page.loginSP()
        home_page.homepage()
        log.info("User is redirected to the Homepage!!")
        self.click_linktext('Add Supplier')
        log.info("Adds Supplier link is clicked from the menu")
        self.adddata_id("_companyName", getsupplierexceldata["CompanyName"])
        log.info("Company name has been added into the textbox!! --> " + getsupplierexceldata["CompanyName"])
        self.adddata_id("_tdLegalName", getsupplierexceldata["CompanyLegalName"])
        log.info("Company Legal Name has been added into the textbox!!" + getsupplierexceldata["CompanyLegalName"])
        self.adddata_id("_street1", getsupplierexceldata["Street1"])
        log.info("Street 1 has been added into the textbox!!" + getsupplierexceldata["Street1"])
        self.adddata_id("_street2", getsupplierexceldata["Street2"])
        log.info("Street 2 has been added into the textbox!!" + getsupplierexceldata["Street2"])
        self.adddata_id("_city", getsupplierexceldata["City"])
        log.info("City has been added into the textbox!!" + getsupplierexceldata["City"])
