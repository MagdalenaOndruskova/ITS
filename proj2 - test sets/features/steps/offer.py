#!/usr/bin/env python3
from behave import *
from selenium.webdriver.common.keys import Keys


# Scenario: Show product from homepage
@given("a web browser is at e-shop homepage")
def step(context):
    context.driver.get("http://pat.fit.vutbr.cz:8083/")


@when('customer clicks on "MacBook"')
def step(context):
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .img-responsive").click()


@then("page with product details is shown")
def step(context):
    assert("MacBook" == context.driver.find_element_by_xpath("//h1").text)


# Scenario: Search product from search bar
@when('customer searchs "MacBook"')
def step_impl(context):
    search_bar = context.driver.find_element_by_name("search")
    search_bar.send_keys('MacBook')
    search_bar.send_keys(Keys.ENTER)


@then("page with MacBook products are shown")
def step_impl(context):
    macbook_number = 1
    for macbook in context.table:
        product_from_page = context.driver.find_element_by_xpath(
            "//div[@id='content']/div[2]/div[" + str(macbook_number) + "]/div/div[2]/div/h4/a").text
        assert(macbook["product"] == product_from_page)
        macbook_number += 1


# Scenario: Show not-empty category
@when('customer clicks on "Phones & PDAs"')
def step_impl(context):
    context.driver.find_element_by_css_selector("li:nth-child(6) > a").click()


@then('page with Phones & PDAs products are shown')
def step_impl(context):
    product_number = 1
    for product in context.table:
        product_from_page = context.driver.find_element_by_xpath("//div[@id='content']/div[2]/div[" +
                                                                 str(product_number) + "]/div/div[2]/div/h4/a").text
        print(product["products"])
        print(product_from_page)
        assert(product["products"] == product_from_page)
        product_number += 1


# Scenario: Show empty category
@when('customer clicks on "Software"')
def step_impl(context):
    context.driver.find_element_by_link_text("Software").click()


@then('customer is shown text: "There are no products to list in this category."')
def step_impl(context):
    expected_text = "There are no products to list in this category."
    got_text = context.driver.find_element_by_xpath("//div/p").text
    assert(expected_text == got_text)


# Scenario: Show subcategory list
@when('customer clicks on "Desktop"')
def step_impl(context):
    context.driver.find_element_by_link_text("Desktops").click()


@then('dropmenu is shown containing subcategories')
def step_impl(context):
    number_of_subcategory = 1
    for subcategory in context.table:
        got_subcategory = context.driver.find_element_by_xpath(
            "//li/div/div/ul/li[" + str(number_of_subcategory) + "]/a").text
        print(subcategory["subcategory"])
        print(got_subcategory)
        assert(subcategory["subcategory"] == got_subcategory)
        number_of_subcategory += 1


# Scenario: Show not-empty subcategory
@given('"Desktop" dropmenu is shown')
def step_impl(context):
    context.driver.find_element_by_link_text("Desktops").click()


@when('customer clicks on "Mac"')
def step_impl(context):
    context.driver.find_element_by_link_text("Mac (1)").click()


@then('page with following Mac products is shown')
def step_impl(context):
    product_number = 1
    for product in context.table:
        got_product = context.driver.find_element_by_xpath("//div[@id='content']/div[2]/div[" + str(product_number) +
                                                           "]/div/div[2]/div/h4/a").text
        assert (product["iMacProd"] == got_product)
        product_number += 1


# Scenario: Show empty subcategory #TODO - čo to spraví ak then už bolo definované?
@when('customer clicks on "PC"')
def step_impl(context):
    context.driver.find_element_by_link_text("PC (0)").click()
