from pdf.utils import read_variable_from_config
from pdf.virtual_page import VirtualPage


class MainPage(VirtualPage):

    def __init__(self, driver, url):

        super().__init__(driver)
        self.url = url

        self.add_element("PatentSearchLogo", "//*[@i18n-txt='system.semanticsearch.title']")
        self.add_element("LoginButton", "(//*[@i18n-txt='login' or @i18n-txt='system.login'])[1]")
        self.add_element("LoginEmail", "//*[contains(@id, 'login') and not(contains(@style, 'none'))]//input[@id='signName']")
        self.add_element("LoginPassword", "//*[contains(@id, 'login') and not(contains(@style, 'none'))]//input[@id='signPass']")
        self.add_element("LoginSubmit", "//*[contains(@id, 'login') and not(contains(@style, 'none'))]//*[@i18n-txt='system.login']")
        self.add_element("UserIcon", "//*[contains(@class, 'user-name-represent') or contains(@class, 'header-user-name')]")

    def navigate(self):
        self.op.navigate_to(self.url)
        self.op.wait_for(self.get_element("PatentSearchLogo"))

    def is_logged_in(self):
        if self.op.is_exist(self.get_element("UserIcon")):
            return True
        else:
            return False

    def login(self, account, password):
        if self.is_logged_in():
            return
        else:
            self.op.click_and_wait_for(self.get_element("LoginButton"), self.get_element("LoginEmail"))
            self.op.send_text(self.get_element("LoginEmail"), account)
            self.op.send_text(self.get_element("LoginPassword"), password)
            self.op.click_and_wait_for(self.get_element("LoginSubmit"), self.get_element("UserIcon"))
            self.op.wait_for(self.get_element("UserIcon"))

    def login_as_unlimited_user(self):
        self.login(read_variable_from_config('UNLIMITED_USER'), read_variable_from_config('UNLIMITED_PASSWORD'))
