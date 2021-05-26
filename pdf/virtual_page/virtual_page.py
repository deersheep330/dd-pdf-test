from pdf.element import Element
from pdf.operations import Operations


class VirtualPage():

    def __init__(self, driver):
        self.driver = driver
        self.elements = {}
        self.url = None
        self.op = Operations(self.driver)

    def add_element(self, name, xpath):
        self.elements[name] = Element(name, xpath)

    def get_element(self, name):
        return self.elements[name]
