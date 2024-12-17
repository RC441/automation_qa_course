import time

from pages.alerts_frames_windows_page import BrowserWindowsPage


class TestAlertsFramesWindow:
    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab_of_window("tab")
            assert text_result == 'This is a sample page', "The new tab has not opened or incorrect tab has opened"

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab_of_window("window")
            assert text_result == 'This is a sample page', "The new window has not opened or incorrect window has opened"


