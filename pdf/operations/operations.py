import json

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep as _sleep


class Operations():

    def __init__(self, driver):

        self.driver = driver
        self.action = ActionChains(driver)
        self.capabilities = driver.capabilities

        self.target_timeout = 10
        self.wait_for_timeout = 10
        self.click_retry_timeout = 3
        self.click_max_retry = 10
        self.poll_frequency = 0.1

        self.default_handle = None

    def __simple_click(self, target_element, x_offset=0, y_offset=0):
        target_element.click();
        #self.action.move_to_element_with_offset(target_element, x_offset, y_offset).click().perform()

    def __context_click(self, target_element, x_offset=0, y_offset=0):
        self.action.move_to_element_with_offset(target_element, x_offset, y_offset).context_click().perform()

    def __click_and_hold(self, target_element, x_offset=0, y_offset=0):
        self.action.move_to_element_with_offset(target_element, x_offset, y_offset).click_and_hold().perform()

    def __move_to_element(self, target_element, x_offset=0, y_offset=0):
        self.action.move_to_element_with_offset(target_element, x_offset, y_offset).perform()

    def click_and_hold(self, target):
        self.__click_with_offset_and_wait_for(target, 0, 0, None, self.target_timeout, self.wait_for_timeout, 'CLICK_AND_HOLD', 'PRESENT')

    def click_and_hold_with_offset(self, target, x_offset, y_offset):
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, None, self.target_timeout, self.wait_for_timeout, 'CLICK_AND_HOLD', 'PRESENT')

    def click_and_hold_and_wait_for(self, target, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, 0, 0, wait_for, self.target_timeout, wait_for_timeout, 'CLICK_AND_HOLD', 'PRESENT')

    def click_and_hold_with_offset_and_wait_for(self, target, x_offset, y_offset, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, wait_for, self.target_timeout, wait_for_timeout, 'CLICK_AND_HOLD', 'PRESENT')

    def release_after_hold(self, target):
        self.action.release(self.find_element(target)).perform()

    def hover(self, target):
        self.__click_with_offset_and_wait_for(target, 0, 0, None, self.target_timeout, self.wait_for_timeout, 'HOVER', 'PRESENT')

    def hover_with_offset(self, target, x_offset, y_offset):
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, None, self.target_timeout, self.wait_for_timeout, 'HOVER', 'PRESENT')

    def hover_and_wait_for(self, target, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, 0, 0, wait_for, self.target_timeout, wait_for_timeout, 'HOVER', 'PRESENT')

    def hover_with_offset_and_wait_for(self, target, x_offset, y_offset, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, wait_for, self.target_timeout, wait_for_timeout, 'HOVER', 'PRESENT')

    def context_click(self, target):
        self.__click_with_offset_and_wait_for(target, 0, 0, None, self.target_timeout, self.wait_for_timeout, 'CONTEXT_CLICK', 'PRESENT')

    def context_click_with_offset(self, target, x_offset, y_offset):
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, None, self.target_timeout, self.wait_for_timeout, 'CONTEXT_CLICK', 'PRESENT')

    def context_click_and_wait_for(self, target, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, 0, 0, wait_for, self.target_timeout, wait_for_timeout, 'CONTEXT_CLICK', 'PRESENT')

    def context_click_with_offset_and_wait_for(self, target, x_offset, y_offset, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, wait_for, self.target_timeout, wait_for_timeout, 'CONTEXT_CLICK', 'PRESENT')

    def keep_clicking_until_disappear(self, target):
        while self.is_exist(target):
            self.click(target)
            _sleep(2)

    def click(self, target):
        self.__click_with_offset_and_wait_for(target, 0, 0, None, self.target_timeout, self.wait_for_timeout, 'CLICK', 'PRESENT')

    def click_with_offset(self, target, x_offset, y_offset):
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, None, self.target_timeout, self.wait_for_timeout, 'CLICK', 'PRESENT')

    def click_and_wait_for(self, target, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, 0, 0, wait_for, self.target_timeout, wait_for_timeout, 'CLICK', 'PRESENT')

    def click_and_wait_until_disappear(self, target, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, 0, 0, wait_for, self.target_timeout, wait_for_timeout, 'CLICK', 'DISAPPEAR')

    def click_with_offset_and_wait_for(self, target, x_offset, y_offset, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, wait_for, self.target_timeout, wait_for_timeout, 'CLICK', 'PRESENT')

    def click_with_offset_and_wait_until_disappear(self, target, x_offset, y_offset, wait_for, wait_for_timeout=None):
        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout
        self.__click_with_offset_and_wait_for(target, x_offset, y_offset, wait_for, self.target_timeout, wait_for_timeout, 'CLICK', 'DISAPPEAR')

    def __click_with_offset_and_wait_for(self, target,  x_offset, y_offset, wait_for, target_timeout, wait_for_timeout, click_type, wait_type):

        target_wait = WebDriverWait(
            self.driver,
            timeout=target_timeout,
            poll_frequency=self.poll_frequency,
            ignored_exceptions=[Exception])

        if wait_for is None:
            target_element = target_wait.until(
                expected_conditions.visibility_of_element_located((By.XPATH, target.xpath)),
                f'Try to find " + {target.name} + " but not found ! ')

            self.scroll_to_element_align_center(target)
            if click_type == 'CLICK':
                self.__simple_click(target_element, x_offset, y_offset)
            elif click_type == 'CONTEXT_CLICK':
                self.__context_click(target_element, x_offset, y_offset)
            elif click_type == 'CLICK_AND_HOLD':
                self.__click_and_hold(target_element, x_offset, y_offset)
            elif click_type == 'HOVER':
                self.__move_to_element(target_element, x_offset, y_offset)
            else:
                raise RuntimeError(f'unsupported click_type: {click_type}')
        else:

            success = False
            retry = 0
            while success is not True and retry < self.click_max_retry:

                try:
                    target_element = target_wait.until(
                        expected_conditions.visibility_of_element_located((By.XPATH, target.xpath)),
                        f'Try to find " + {target.name} + " but not found ! ')

                    self.scroll_to_element_align_center(target)

                    if click_type == 'CLICK':
                        self.__simple_click(target_element, x_offset, y_offset)
                    elif click_type == 'CONTEXT_CLICK':
                        self.__context_click(target_element, x_offset, y_offset)
                    elif click_type == 'CLICK_AND_HOLD':
                        self.__click_and_hold(target_element, x_offset, y_offset)
                    elif click_type == 'HOVER':
                        self.__move_to_element(target_element, x_offset, y_offset)
                    else:
                        raise RuntimeError(f'unsupported click_type: {click_type}')

                    wait_for_wait = WebDriverWait(
                        self.driver,
                        timeout=wait_for_timeout,
                        poll_frequency=self.poll_frequency,
                        ignored_exceptions=[Exception])

                    if wait_type == 'PRESENT':
                        wait_for_wait.until(
                            expected_conditions.visibility_of_element_located((By.XPATH, wait_for.xpath)),
                            f'Click {target.name} and Wait for {wait_for.name} Fail!')
                    else:
                        wait_for_wait.until(
                            expected_conditions.invisibility_of_element_located((By.XPATH, wait_for.xpath)),
                            f'Click {target.name} and Wait for {wait_for.name} Disappear Fail!')

                    success = True
                except Exception as e:
                    print(f'{e} retry: {retry}')
                finally:
                    retry += 1

            if success is not True:
                if wait_type == 'PRESENT':
                    raise RuntimeError(f'Click {target.name} and wait for {wait_for.name} fail after timeout {self.click_max_retry * wait_for_timeout} s')
                else:
                    raise RuntimeError(f'Click {target.name} and wait for {wait_for.name} disappearing fail after timeout {self.click_max_retry * wait_for_timeout} s')

    def wait_for(self, wait_for, wait_for_timeout=None):

        if wait_for_timeout is None:
            wait_for_timeout = self.wait_for_timeout

        wait_for_wait = WebDriverWait(
            self.driver,
            timeout=wait_for_timeout,
            poll_frequency=self.poll_frequency,
            ignored_exceptions=[Exception])

        wait_for_wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, wait_for.xpath)),
            f'Element " + {wait_for.name} + " not found after timeout {wait_for_timeout} s.')

        self.scroll_to_element_align_center(wait_for)

    def scroll_to_element_align_center(self, target):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.find_element(target))

    def find_element(self, target):

        if self.try_to_find(target) is False:
            raise RuntimeError(f'Element {target.name} not Found!')

        elements = self.find_elements(target)
        if len(elements) == 1:
            return elements[0]
        else:
            raise RuntimeError('More than one element found! Use find_elements() instead.')

    def find_elements(self, target):

        if self.try_to_find(target) is False:
            raise RuntimeError(f'Element {target.name} not Found!')

        return self.driver.find_elements_by_xpath(target.xpath)

    def try_to_find(self, target, target_timeout=None):

        if target_timeout is None:
            target_timeout = self.target_timeout

        target_wait = WebDriverWait(
            self.driver,
            timeout=target_timeout,
            poll_frequency=self.poll_frequency,
            ignored_exceptions=[Exception])
        try:
            target_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, target.xpath)))
        except Exception:
            pass
        finally:
            return self.is_exist(target)

    def is_exist(self, target):
        if len(self.driver.find_elements_by_xpath(target.xpath)) != 0 and \
           self.driver.find_element_by_xpath(target.xpath).is_displayed():
            return True
        else:
            return False

    def send_text(self, target, text):
        element = self.driver.find_element_by_xpath(target.xpath)
        element.clear()
        element.send_keys(text)

    def drag_and_drop_file(self, target, file_path):
        self.find_element(target).send_keys(file_path)

    def select_dropdown_option_by_value(self, dropdown, value_to_select):
        select = Select(self.find_element(dropdown))
        select.select_by_value(value_to_select)

    def navigate_to(self, url):
        self.driver.get(url)
        self.default_handle = self.driver.current_window_handle

    def reload_page(self):
        self.driver.refresh()

    def is_new_tab_being_opened(self):
        if len(self.driver.window_handles) > 1:
            return True
        else:
            return False

    def get_current_opened_tabs_count(self):
        return len(self.driver.window_handles)

    def get_current_opened_tabs(self):
        return self.driver.window_handles

    def switch_to_first_newly_opened_tab(self):
        for handle in self.driver.window_handles:
            if self.default_handle == handle:
                print(f'switch from {self.default_handle} to handle {handle}')
                self.driver.switch_to.window(handle)
                break

    def close_newly_opened_tabs(self):
        for handle in self.driver.window_handles:
            if self.default_handle != handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(self.default_handle)

    def save_current_tab_as_default_handle(self):
        self.default_handle = self.driver.current_window_handle

    def get_current_tab_handle(self):
        return self.driver.current_window_handle

    def get_default_tab_handle(self):
        return self.default_handle

    def click_alert_ok(self):
        self.driver.switch_to.alert.accept()

    def get_current_url(self):
        return self.driver.get_url()

    def quit(self):
        self.driver.quit()

    def sleep(self, sec):
        _sleep(sec)

    def wait_for_response(self, keyword, wait_for_timeout=60):

        sleep_time = 3
        retry = 0
        max_retry = wait_for_timeout / sleep_time
        while retry < max_retry:
            for entry in self.driver.get_log('performance'):
                message = json.loads(entry['message'])
                if 'message' in message:
                    _message = message['message']
                    if 'params' in _message:
                        params = _message['params']
                        if 'response' in params:
                            response = params['response']
                            if 'url' in response:
                                url = response['url']
                                print(f'{url}')
                                if keyword in url:
                                    print(f'==> get response for {url}')
                                    return
            _sleep(sleep_time)
            retry += 1
        raise RuntimeError(f'wait for response {keyword} timeout after {wait_for_timeout} sec')








