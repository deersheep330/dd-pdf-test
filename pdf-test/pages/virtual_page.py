

class VirtualPage():

    def __init__(self, driver):
        self.driver = driver
        self.elements = {}
        self.url = None
        self.op =