import random
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import ( \
    TextBoxPageLocators, \
    CheckBoxPageLocators, \
    RadioButtonPageLocators, \
    WebTablePageLocators, \
    ButtonsPageLocators \
    )
from pages.base_page import BasePage
# import  time

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def  fill_all_fields(self):
        person_info = next(generated_person())

        full_name         = person_info.full_name
        email             = person_info.email
        current_address   = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        # time.sleep(5)
        return full_name, email, current_address, permanent_address


    def check_filled_form(self):
        full_name         = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email             = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address   = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            title_item = title_item.text
            title_item = str(title_item).replace(' ', '').replace('doc', '').replace('.', '').lower()
            data.append(title_item)
        return data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            item = item.text
            item = str(item).lower()
            data.append(item)
        return data

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()



    def click_on_the_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIO_BUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIO_BUTTON,
            'no': self.locators.NO_RADIO_BUTTON
            }


        radio = self.element_is_visible(choices[choice])
        self.go_to_element(radio)
        radio.click()
        # return radio

    def get_output_result(self):
        return  self.element_is_present(self.locators.OUTPUT_RESULT).text

class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    # Переместить в BasePage.
    def remove_banners(self):
        self.remove_banner(self.locators.BANNER_1_JS)
        # self.remove_banner(self.locators.BANNER_2_JS)
        # self.remove_banner(self.locators.BANNER_3_JS)
        self.remove_banner(self.locators.BANNER_4_JS)


    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())

            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            self.element_is_visible(self.locators.ADD_NEW_RECORD_BUTTON).click()

            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)

            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            # time.sleep(5)

            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]
        # [first_name, last_name, email, str(age), str(salary), department]

    def add_random_count_of_persons(self, min_count, max_count):
        pass

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            self.go_to_element(item)
            data.append(item.text.splitlines())
        return data

    def search_some_person(self, key_word):
        # self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)
        # search_field = self.element_is_visible(self.locators.SEARCH_INPUT)
        # self.go_to_element(search_field)
        # search_field.send_keys(key_word)
        self.go_to_element(self.element_is_visible(self.locators.SEARCH_INPUT))
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

        # Переработать метод. Поиск по значку
    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        self.go_to_element(delete_button)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        self.go_to_element(row)
        return row.text.splitlines()


    # Задание: сделать версию метода для полностью рандомного выбора
    # параметра человека из списка и проверка корректности изменений

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        edit = self.element_is_visible(self.locators.UPDATE_BUTTON)
        self.go_to_element(edit)
        edit.click()
        age_field = self.element_is_visible(self.locators.AGE_INPUT)
        age_field.clear()
        age_field.send_keys(age)
        submit = self.element_is_visible(self.locators.SUBMIT_BUTTON)
        self.go_to_element(submit)
        submit.click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

        # delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        # self.go_to_element(delete_button)
        # delete_button.click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROW_FOUND).text

    def select_up_to_some_rows(self):
        count = [5, 10, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            option = self.element_is_visible((By.CSS_SELECTOR, 'option[value="{x}"]'))
            self.go_to_element(option)
            option.click()
            data.append(self.check_row_count())
        return data

    def check_row_count(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


















