import os
from configparser import ConfigParser
from pdf.pages import MainPage, DdPage


def before_all(context):

    config = ConfigParser()
    config_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(config_file)
    print(f'==> Browser = {config["Environment"]["Browser"]}')

    context.ps_page = MainPage()
    context.dd_page = DdPage()

