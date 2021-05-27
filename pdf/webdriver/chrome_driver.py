from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver():

    def __init__(self, is_headless=True, window_size='1920,1200'):

        options = webdriver.ChromeOptions()

        # prevent notification
        prefs = {'profile.default_content_setting_values.notifications': 2}
        options.add_experimental_option('prefs', prefs)

        # headless
        if is_headless is True:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')

        # window size
        options.add_argument(f'window-size={window_size}')

        # enable logging prefs
        caps = options.to_capabilities()
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}

        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), desired_capabilities=caps)

    def get_driver(self):
        return self.driver
