import os
from configparser import ConfigParser
from pdf.webdriver import ChromeDriver
from pdf.pages import MainPage, DdPage


def before_all(context):

    # browser
    config = ConfigParser()
    config_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(config_file)
    print(f'==> Browser = {config["Environment"]["Browser"]}')
    driver = ChromeDriver(is_headless=False).get_driver()

    # env
    print(f'==> Env = {config["Environment"]["Env"]}')
    main_url = 'https://stage.patentcloud.com/'
    dd_url = 'https://stage.patentcloud.com/dd'

    context.ps_page = MainPage(driver, main_url)
    context.dd_page = DdPage(driver, dd_url)


def after_all(context):
    context.dd_page.quit()