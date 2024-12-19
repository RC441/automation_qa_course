import time

from pages.alerts_frames_windows_page import BrowserWindowsPage, AlertsPage, FramesPage


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


    class TestAlerts:

        def test_click_to_see_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == "You clicked a button", "Alert did not show up"


        def test_wait_for_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_wait_for_alert_for_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Alert did not show up"


        def test_click_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alert_text = alerts_page.check_confirm_alert()
            print(alert_text)
            assert alert_text == "You selected Ok" or "You selected Cancel", "Alert did not show up"



        def test_prompt_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            text_entered, text_alert = alerts_page.check_prompt_alert()
            # print(text_entered)
            # print(text_alert)
            assert text_entered in text_alert, "Alert did not show up"

    class TestFrames:

        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            result_frame1 = frames_page.check_frame('frame1')
            result_frame2 = frames_page.check_frame('frame2')
            # print(result_frame1)
            # print(result_frame2)
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'Frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'Frame does not exist'








