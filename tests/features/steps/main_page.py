from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given(u'that I go to the landing page')
def step_impl(context):
    # Get main page
    context.driver.get(context.url)
    time.sleep(2)


@when(u'I go to the navigation bar')
def step_impl(context):
    # Get NavBar
    context.navBar = context.driver.find_element(By.CLASS_NAME, "nav-primary")


@then(u'I see the links "{links}".')
def step_imp(context, links):
    not_working = []
    # Separate the links.
    parsed_links = links.split(", ")
    # Get all the links in the NavBar
    elements = context.navBar.find_elements(By.TAG_NAME, "a")
    for element in elements:
        # Get link text
        inner = element.get_attribute('innerHTML')
        # Compare with the expected links
        if inner not in parsed_links:
            not_working.append(inner)

    assert len(not_working) == 0, f'{not_working} not found in expected links.'


@when(u'I go to the title')
def step_impl(context):
    try:
        # Get the main title.
        title = context.driver.find_element(By.TAG_NAME, "h1")
        context.title = title.text
    except BaseException:
        context.title = ""


@then(u'I can see the title "The Connected TV App Experts".')
def step_impl(context):
    # Comparing with the requiriment.
    flag = True if context.title == "The\nConnected\nTV\nApp\nExperts" else False
    assert flag, f'unexpected title: {context.title}'


@when(u'I scroll to the contact form')
def step_impl(context):
    # Get the form.
    context.form = context.driver.find_element(By.TAG_NAME, "form")


@then(u'I can see a form with the fields "{fields}"')
def step_impl(context, fields):
    missing = []
    # Gives format to the expected form fields.
    parsed_fields = fields.split(", ")

    elements = context.form.find_elements(By.TAG_NAME, "li")
    # Gives format to the found fields.
    parsed_elements = [element.text for element in elements]

    # Compare expected felds with the found fields.
    for field in parsed_fields:
        if field not in parsed_elements:
            missing.append(field)

    assert len(missing) == 0, f'Missing fields: {missing}'


@then(u'I can see a "{button}" button.')
def step_impl(context, button):
    # Get the button from the form-
    send_btn = context.form.find_element(By.TAG_NAME, "button")
    # Compare the button type and button text.
    flag = send_btn.get_attribute(
        'type') == 'submit' and send_btn.text == button

    assert flag, f'Wrong button info.'
