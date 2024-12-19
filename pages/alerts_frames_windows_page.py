import random
import time

from selenium.common import TimeoutException, UnexpectedAlertPresentException

from locators.alerts_frames_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()


    def check_opened_new_tab_of_window(self, choice):
        if choice == 'tab':
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        if choice == 'window':
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.SAMPLE_PAGE_TEXT).text
        return  text_title

class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    # # var1 - works
    # def check_wait_for_alert_for_5_sec (self):
    #     self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
    #     time.sleep(5)
    #     alert_text = self.driver.switch_to.alert.text
    #     return alert_text

    # var2 - works
    def check_wait_for_alert_for_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        try:
            alert_window= self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        # alert_window.accept()
        # alert_window.dismiss()
        x = random.choice([True, False])
        if x:
            print("Выбрано: accept()")
            alert_window.accept()  # press Of
        else:
            print("Выбрано: dismiss()")
            alert_window.dismiss()  # press Cancel

        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):
        text = f'autotest-{random.randint(0, 999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_visible(self.locators.PROMPT_RESULT).text
        return text, text_result



