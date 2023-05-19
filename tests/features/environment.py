from selenium import webdriver
from behave import fixture, use_fixture
from selenium.webdriver import Chrome


@fixture
def browser_chrome(context):
    # Default Options
    options = webdriver.ChromeOptions()
    context.driver = Chrome(options=options)
    # Main URL
    context.url = 'https://fxdigital.uk/'
    yield context


def before_all(context):
    use_fixture(browser_chrome, context)
