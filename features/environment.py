from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # allows chrome driver installation via API


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


def before_step(context, step):
    context.driver.implicitly_wait(7)