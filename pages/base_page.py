from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    # def switch_to_new_tab(self):








    # banners remove
    def remove_banner(self, locator):
        # js = "document.querySelector(" + locator + ").remove()"
        js = locator
        self.driver.execute_script(js)

        # element = self.element_is_present("div[id='square']")  #'.GoogleActiveViewElement'
        # if element:
        #     js = "document.querySelector('div[id='square']').remove()"
        #     self.driver.execute_script(js)
        # # time.sleep(6)

    # def remove_banner(self):
    #     # js = "document.querySelector(" + locator + ").remove()"
    #     # self.driver.execute_script(js)
    #
    #     element = self.element_is_present("div[id='square']")  #'.GoogleActiveViewElement'
    #     if element:
    #         js = "document.querySelector('div[id='square']').remove()"
    #         self.driver.execute_script(js)
    #     # time.sleep(6)



