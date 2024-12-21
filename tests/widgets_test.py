import time

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')

            assert first_title == 'What is Lorem Ipsum?' and len(first_content) > 0, "Incorrect title or missing text"
            assert second_title == 'Where does it come from?' and len(second_content) > 0, "Incorrect title or missing text"
            assert third_title == 'Why do we use it?' and len(third_content) > 0, "Incorrect title or missing text"




    class TestAutoCompletePage:

        def test_full_multi_autocomplete_field_with_one_color(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_multi_autocomplete_field_one_color()
            colors_result = autocomplete_page.check_color_in_multi()
            # print(colors)
            # print(colors_result)
            assert colors == colors_result

        def test_full_multi_autocomplete_field_with_multiple_colors(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            colors = autocomplete_page.fill_multi_autocomplete_field_multiple_colors()
            colors_result = autocomplete_page.check_color_in_multi()
            # print(colors)
            # print(colors_result)
            assert colors == colors_result, "The added colors are missing in the input"

        def test_remove_one_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_multi_autocomplete_field_multiple_colors()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            # print(count_value_before)
            # print(count_value_after)
            assert count_value_before > count_value_after, "Value was not deleted"


        def test_remove_all_values_from_multi_one_by_one(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            autocomplete_page.fill_multi_autocomplete_field_multiple_colors()
            count_value_before, count_value_after = autocomplete_page.remove_all_value_from_multi()
            # print(count_value_before)
            # print(count_value_after)
            assert count_value_after == 0, "Values was not deleted"

        # def test_remove_all_values_from_multi_at_once(self, driver):
        #     autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        #     autocomplete_page.open()

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            autocomplete_page.open()
            color = autocomplete_page.fill_single_autocomplete_field()
            color_result = autocomplete_page.check_color_in_single()
            # print(color)
            # print(color_result)
            assert color == color_result, "The added colors are missing in the input"












