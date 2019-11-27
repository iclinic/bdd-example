# pylint: disable=function-redefined
# pylint: disable=no-name-in-module
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('que entrei no site do "GitHub"')
def step_impl(context):
    context.driver.get("https://github.com/")


@when('procurar por {rep}')
def step_impl(context, rep):
    context.driver.find_element(By.NAME, 'q').send_keys(rep)
    context.driver.find_element(
        By.CSS_SELECTOR, '#jump-to-suggestion-search-global .js-jump-to-badge-search').click()


@then('o repositório será encontrado')
def step_impl(context):
    assert context.driver.find_element(
        By.CSS_SELECTOR, 'a[class="v-align-middle"][href="/iclinic/bdd-example"]')
    sleep(5)