#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""
context.driver = webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
                                      desired_capabilities=DesiredCapabilities.CHROME)
"""


def before_all(context):
    context.driver = webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub',
                                      desired_capabilities=DesiredCapabilities.CHROME)
    context.driver.implicitly_wait(15)
    context.base_url = "http://pat.fit.vutbr.cz:8083/"


def after_all(context):
    context.driver.quit()
