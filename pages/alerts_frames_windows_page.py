from locators.alerts_frames_windows_locators import BrowserWindowsPageLocators
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



