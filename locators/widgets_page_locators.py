from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST_HEADING = (By.CSS_SELECTOR, "div[id='section1Heading']")
    SECTION_FIRST_CONTENT = (By.CSS_SELECTOR, "div[id='section1Content'] p")

    SECTION_SECOND_HEADING = (By.CSS_SELECTOR, "div[id='section2Heading']")
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, "div[id='section2Content'] p")

    SECTION_THIRD_HEADING = (By.CSS_SELECTOR, "div[id='section3Heading']")
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, "div[id='section3Content'] p")
