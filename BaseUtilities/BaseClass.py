import inspect
import logging
import sys
import unittest

import pytest

@pytest.mark.usefixtures("setup")
class BaseClass:

    def click_id(self, locator):
        return self.driver.find_element_by_id(locator).click()

    def click_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator).click()

    def click_linktext(self, locator):
        return self.driver.find_element_by_link_text(locator).click()

    def multiple_elements_xpath(self, locator):
        return self.driver.find_elements_by_xpath(locator)

    def adddata_id(self, locator, value):
        return self.driver.find_element_by_id(locator).send_keys(value)

    def adddata_name(self, locator, value):
        return self.driver.find_element_by_name(locator).send_keys(value)

    def adddata_xpath(self, locator, value):
        return self.driver.find_element_by_xpath(locator).send_keys(value)

    @staticmethod
    def getLogger():

        logger_name = inspect.stack()[1][3]
        log = logging.getLogger(logger_name)
        File_handler = logging.FileHandler('logfile.log')
        formatting = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        File_handler.setFormatter(formatting)
        log.setLevel(logging.DEBUG)

    # Logs in Console
        Stream_handler = logging.StreamHandler(sys.stdout)
        Formatting = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        Stream_handler.setFormatter(Formatting)
        if not log.handlers:
            log.addHandler(File_handler)
            log.addHandler(Stream_handler)
        log.setLevel(logging.INFO)
        return log
