from behave import *


# Scenario: Customer Account options
@when('customer clicks on "My account"')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a/span[2]").click()


@then('user is shown the dropmenu My Account  with following subcategories')
def step_impl(context):
    number_opt = 1
    for option in context.table:

        given_opt = context.driver.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/ul/li[" +
                                                                 str(number_opt) + "]/a").text
        print("aaaa" + option["MyAccountSub"])
        print("bbbbb" +given_opt)
        assert(option["MyAccountSub"] == given_opt)
        number_opt += 1


# Scenario: Registration of new customer - Without filling required fields
@given("a web browser is at registration page")
def step_impl(context):
    context.driver.get("http://pat.fit.vutbr.cz:8083/index.php?route=account/register")


@given("First Name field is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//fieldset[@id='account']/div[2]/div/input").clear()


@given("Last Name field is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//fieldset[@id='account']/div[3]/div/input").clear()


@given("EMail field is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//fieldset[@id='account']/div[4]/div/input").clear()


@given("Telephone field is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//fieldset[@id='account']/div[5]/div/input").clear()


@given("Address 1 field is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//fieldset[@id='address']/div[2]/div/input").clear()


@given("City field is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//fieldset[@id='address']/div[4]/div/input").clear()


@given("Post Code field is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//fieldset[@id='address']/div[5]/div/input").clear()


@given("Password field is empty")
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@id='content']/form/fieldset[3]/div/div/input").clear()


@when('customer clicks on "Continue"')
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@value='Continue']").click()


@then("warnings bellow First Name field is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[2]/div/div").text
    assert(text == "First Name must be between 1 and 32 characters!")


@then("warnings bellow Last Name field is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[3]/div/div").text
    assert (text == "Last Name must be between 1 and 32 characters!")


@then("warnings bellow EMail field is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[4]/div/div").text
    assert (text == "E-Mail Address does not appear to be valid!")


@then("warnings bellow Telephone field is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//fieldset[@id='account']/div[5]/div/div").text
    assert (text == "Telephone must be between 3 and 32 characters!")


@then("warnings bellow Address 1 field is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[2]/div/div").text
    assert (text == "Address 1 must be between 3 and 128 characters!")


@then("warnings bellow City field is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[4]/div/div").text
    assert (text == "City must be between 2 and 128 characters!")


@then("warnings bellow Post Code field is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//fieldset[@id='address']/div[5]/div/div").text
    assert (text == "Postcode must be between 2 and 10 characters!")


@then("warnings bellow Password field is displayed")
def step_impl(context):
    text = context.driver.find_element_by_xpath("//div[@id='content']/form/fieldset[3]/div/div/div").text
    assert (text == "Password must be between 4 and 20 characters!")


# Scenario: Registration of new customer - Not agreeing to Privacy Policy
@given("required fields are filled")
def step_impl(context):
    context.driver.find_element_by_id("input-firstname").send_keys("Anna")
    context.driver.find_element_by_id("input-lastname").send_keys("Hraskova")
    context.driver.find_element_by_id("input-email").send_keys("anahraskova@gmail.com")
    context.driver.find_element_by_id("input-telephone").send_keys("12358")
    context.driver.find_element_by_id("input-address-1").send_keys("City 25")
    context.driver.find_element_by_id("input-city").send_keys("New City")
    context.driver.find_element_by_id("input-country").send_keys("label=Slovak Republic")
    context.driver.find_element_by_id("input-zone").send_keys("label=Trnavský")
    context.driver.find_element_by_id("input-password").send_keys("Heslo")
    context.driver.find_element_by_id("input-confirm").send_keys("Heslo")


@then('a warning is shown: "Warning: You must agree to the Privacy Policy!"')
def step_impl(context):
    warning = context.driver.find_element_by_xpath("//body/div[2]/div").text
    assert("Warning: You must agree to the Privacy Policy!" == warning)
