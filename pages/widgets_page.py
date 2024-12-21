import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first' :
                         {'title':self.locators.SECTION_FIRST_HEADING,
                          'content':self.locators.SECTION_FIRST_CONTENT},
                     'second':
                         {'title': self.locators.SECTION_SECOND_HEADING,
                          'content': self.locators.SECTION_SECOND_CONTENT},
                     'third':
                         {'title': self.locators.SECTION_THIRD_HEADING,
                          'content': self.locators.SECTION_THIRD_CONTENT}
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text

        # print(section_title.text)
        # print(section_content)
        return [section_title.text, section_content]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_multi_autocomplete_field_one_color(self):
        # color = next(generated_color()).color_name
        color = random.sample(next(generated_color()).color_name, k=1)
        input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
        input_multi.send_keys(color)
        input_multi.send_keys(Keys.ENTER)
        return color


    def fill_multi_autocomplete_field_multiple_colors(self):
        count_to_pick =  random.randint(2, 6)
        colors = random.sample(next(generated_color()).color_name, k=count_to_pick)
        current_color_list = []
        for color in colors:
            input_multi = self.element_is_visible(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
            current_color_list.append(color)
        return current_color_list

    # var1
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.REMOVE_VALUE_MULTI)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    # # var2
    # def remove_value_from_multi(self):
    #     count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
    #     remove_button_list = self.elements_are_visible(self.locators.REMOVE_VALUE_MULTI)
    #     remove_button_list_count = len(remove_button_list)
    #     for value in remove_button_list:
    #         while (True):
    #             value.click()
    #             if (len(remove_button_list) > 1):
    #                 continue
    #             else:
    #                 break
    #         # if remove_button_list_count > 2:
    #         #     value.click()
    #         # if remove_button_list_count == 2:
    #         #     break
    #     count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
    #     return count_value_before, count_value_after


    #remove all items in the field one by one
    def remove_all_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.REMOVE_VALUE_MULTI)
        count_value_after = count_value_before
        for value in remove_button_list:
            value.click()
            count_value_after = count_value_after-1
        return count_value_before, count_value_after

    # #remove all items in the field at once
    # def remove_all_value_from_multi(self):
    #     count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
    #     clear_multi_field = self.element_is_visible(self.locators.CLEAR_MULTI_FIELD)
    #     count_value_after = count_value_before
    #     for value in remove_button_list:
    #         value.click()
    #         count_value_after = count_value_after-1
    #     return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list =  self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors


    def fill_single_autocomplete_field(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text











