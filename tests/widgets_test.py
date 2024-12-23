import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


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


    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            # print(value_date_before)
            # print(value_date_after)
            assert value_date_before != value_date_after, "Date and time has not been changed"

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            # print(value_date_before)
            # print(value_date_after)
            assert value_date_before != value_date_after, "Date and time has not been changed"


    class TestSliderPage:

        def test_slider(self, driver):
            slider = SliderPage(driver, "https://demoqa.com/slider")
            slider.open()
            before, after, tooltip = slider.change_slider_value()
            # print("Before: " + str(before))
            # print("After: " + str(after))
            # print("Tooltip: " + str(tooltip))
            assert before != after, "The slider value has not been changed"
            assert tooltip == after, "The tooltip value does not match to actual slider value"



    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after, "The progress bar value has not been changed"


    class TestTabsPage:

        def test_tabs(self, driver):
            tabs = TabsPage(driver, "https://demoqa.com/tabs")
            tabs.open()
            what_button, what_content = tabs.check_tabs("what")
            origin_button, origin_content = tabs.check_tabs("origin")
            use_button, use_content = tabs.check_tabs("use")
            # more_button, more_content = tabs.check_tabs("more")
            assert what_button == "What" and what_content != 0, "The tab 'What' was not pressed or the text is missing"
            assert origin_button == "Origin" and origin_content != 0, "The tab 'Origin' was not pressed or the text is missing"
            assert use_button == "Use" and use_content != 0, "The tab 'Use' was not pressed or the text is missing"

    class TestToolTipsPage:

        # BROKEN
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()

            # #var1
            # button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            # print(button_text)
            # print(field_text)
            # print(contrary_text)
            # print(section_text)

            # var2
            button_text =  tool_tips_page.check_tool_tips("button")
            field_text =  tool_tips_page.check_tool_tips("field")
            contrary_text = tool_tips_page.check_tool_tips("contrary")
            section_text = tool_tips_page.check_tool_tips("section")
            print(button_text)
            print(field_text)
            print(contrary_text)
            print(section_text)

            # # test
            # field_text = tool_tips_page.check_tool_tips()
            # print(field_text)

            # assert button_text   == "You hovered over the Button", "The hover is missing or has incorrect content"
            # assert field_text    == "You hovered over the text field", "The hover is missing or has incorrect content"
            # assert contrary_text == "You hovered over the Contrary", "The hover is missing or has incorrect content"
            # assert section_text  == "You hovered over the 1.10.32", "The hover is missing or has incorrect content"



    class TestMenuPage:

        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu#")
            menu_page.open()
            data = menu_page.check_menu()
            # print(data)
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2',
         'Main Item 3'], "Menu items do not exist or have not been selected"












