import time

from pages.form_page import FormPage


class TestForm:
    class TestFormPage:

        def test_form(self, driver):
            form_page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            form_page.open()
            person_data = form_page.fill_form_fields()
            result = form_page.form_result()
            print(person_data.first_name, person_data.last_name, person_data.email)
            print(result[0], result[1])
            person_info = [person_data.first_name + " " + person_data.last_name, person_data.email]
            result_form_info = [result[0], result[1]]
            assert person_info == result_form_info, "The form has not been filled"



