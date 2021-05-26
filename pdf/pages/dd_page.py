from pdf.utils import read_variable_from_config
from pdf.virtual_page import VirtualPage


class DdPage(VirtualPage):

    def __init__(self, driver, url):

        super().__init__(driver)
        self.url = url