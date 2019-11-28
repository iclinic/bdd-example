from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def before_scenario(context, scenario):
    context.driver.maximize_window()


def before_step(context, step):
    context.driver.implicitly_wait(7)
