from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST_HEADING = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")

    SECTION_SECOND_HEADING = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")

    SECTION_THIRD_HEADING = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
    MULTI_VALUE = (By.CSS_SELECTOR, "div[class='css-12jo7m5 auto-complete__multi-value__label']")
    MULTI_INPUT_VALUES = (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
    REMOVE_VALUE_MULTI = (By.CSS_SELECTOR, "div[class='css-xb97g8 auto-complete__multi-value__remove']")
    CLEAR_MULTI_FIELD = (By.CSS_SELECTOR, ".auto-complete__indicators path")

    SINGLE_CONTAINER = (By.CSS_SELECTOR, "input[id='autoCompleteSingleContainer']")
    SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")
    SINGLE_VALUE = (By.CSS_SELECTOR, "div[class='auto-complete__single-value css-1uccc91-singleValue']")


