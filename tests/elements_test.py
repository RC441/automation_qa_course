import random
import time
from itertools import count

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_cur_addr)
            print(output_per_addr)

            assert full_name == output_name, "The Full Name does not match"
            assert email == output_email, "The Email does not match"
            assert current_address == output_cur_addr, "The Current Address does not match"
            assert permanent_address == output_per_addr, "The Permanent Address does not match"


            # time.sleep(3)

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, "Checkboxes haven't been selected"

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            # time.sleep(3)
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            # time.sleep(3)
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            # time.sleep(3)
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            # time.sleep(3)
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"





    class TestWebTable:

        def test_web_table_add_person(self,driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            # time.sleep(3)
            print(table_result)
            assert new_person in table_result

            # СЛОМАН ИЗ-ЗА БАННЕРОВ
            #тест поломан хотя логика правильная. баннеры перекрывают элементы
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.remove_banners()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            time.sleep(1)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "The person wasn't found in the table"

        # СЛОМАН ИЗ-ЗА БАННЕРОВ
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.remove_banners()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            # print(age)
            # print(row)
            assert age in row, "The person's card has not been changed"

        # СЛОМАН ИЗ-ЗА БАННЕРОВ
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        # СЛОМАН ИЗ-ЗА БАННЕРОВ
        def test_web_table_change_row_count(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            web_table_page.remove_banners()
            row_count = web_table_page.select_up_to_some_rows()
            assert row_count == [5, 10, 25, 50, 100], 'The number of row in the table has not been changed or has changed incorrectly'




