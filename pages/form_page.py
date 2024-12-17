import os

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()

        # remove footer
        # self.remove_footer()

        # first name
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        # last name
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        # email
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        # gender
        self.element_is_visible(self.locators.GENDER).click()
        # mobile (10 Digits)
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)

        # date of birth
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).clear()
        # self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys("20 apr 1984")
        # self.element_is_visible(self.locators.DATE_PICKER).send_keys(Keys.RETURN)

        # subjects
        self.element_is_visible(self.locators.SUBJECT).send_keys("Maths")
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)

        # hobbies (Sports Reading Music)
        self.element_is_visible(self.locators.HOBBIES).click()

        # picture
        self.element_is_visible(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)

        # current address
        # current_address = self.element_is_visible(self.locators.CURRENT_ADDRESS)
        # self.go_to_element(self.element_is_present(self.locators.CURRENT_ADDRESS))
        # current_address.send_keys(person.current_address)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)

        # state and city
        # select state
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        # select city
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        # submit button
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person


    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data














