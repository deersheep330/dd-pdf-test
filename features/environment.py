import os
from configparser import ConfigParser
from pdf.webdriver import ChromeDriver
from pdf.pages import MainPage, DDPage


def before_all(context):

    main_url = 'https://stage.patentcloud.com/'
    dd_url = 'https://stage.patentcloud.com/dd'

    # browser
    config = ConfigParser()
    config_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(config_file)
    print(f'==> Browser = {config["Environment"]["Browser"]}')
    driver = ChromeDriver(is_headless=False).get_driver()

    # env
    env = config["Environment"]["Env"]
    print(f'==> Env = {env}')
    if env == 'Stage':
        main_url = 'https://stage.patentcloud.com/'
        dd_url = 'https://stage.patentcloud.com/dd'
    elif env == 'Production':
        main_url = 'https://app.patentcloud.com/'
        dd_url = 'https://app.patentcloud.com/dd'

    context.ps_page = MainPage(driver, main_url)
    context.dd_page = DDPage(driver, dd_url)


def after_all(context):
    context.dd_page.quit()