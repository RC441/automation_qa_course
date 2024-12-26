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

class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, ".react-datepicker__time-list-item")  #li[class='react-datepicker__time-list-item']
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")

class SliderPageLocators:
    # slider
    SLIDER_INPUT = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input[id='sliderValue']")
    SLIDER_TOOLTIP = (By.CSS_SELECTOR, "div[class='range-slider__tooltip__label']")


class ProgressBarPageLocators:
    #progressbar
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, "button[id='startStopButton']")
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")


class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")

    TABS_ORIGIN = (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")

    TABS_USE = (By.CSS_SELECTOR, "a[id='demo-tab-use']")
    TABS_USE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")

    TABS_MORE = (By.CSS_SELECTOR, "a[id='demo-tab-more']")
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")

class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, "button[id='toolTipButton']")
    BUTTON_TOOL_TIP = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")

    FIELD = (By.CSS_SELECTOR, "div[id='texFieldToolTopContainer'] input[id='toolTipTextField']")
    FIELD_TOOL_TIP = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")

    CONTRARY_LINK = (By.XPATH, "//*[.='Contrary']")
    CONTRARY_LINK_TOOL_TIP = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")

    SECTION_LINK = (By.XPATH, "//*[.='1.10.32']")
    SECTION_LINK_TOOL_TIP = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")

    TOOL_TIP_INNERS = (By.CSS_SELECTOR, "div[class='tooltip-inner']")


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")


class SelectMenuPageLocators:
    # Select Value (dropdown list)
    SELECT_VALUE_DROPDOWN_MENU = (By.CSS_SELECTOR, "div[id='withOptGroup']")
    GROUP_1_OPTION_1 =    (By.CSS_SELECTOR, "div[id='react-select-2-option-0-0")
    GROUP_1_OPTION_2 =    (By.CSS_SELECTOR, "div[id='react-select-2-option-0-1")
    GROUP_2_OPTION_1 =    (By.CSS_SELECTOR, "div[id='react-select-2-option-1-0")
    GROUP_2_OPTION_2 =    (By.CSS_SELECTOR, "div[id='react-select-2-option-1-1")
    ROOT_OPTION =         (By.CSS_SELECTOR, "div[id='react-select-2-option-2")
    ANOTHER_ROOT_OPTION = (By.CSS_SELECTOR, "div[id='react-select-2-option-3")

    # Select One (select title/ dropdown menu)
    SELECT_TITLE_DROPDOWN_MENU = (By.CSS_SELECTOR, "div div[id='selectOne']")
    DR_SELECT    = (By.CSS_SELECTOR, "div div[id='react-select-3-option-0-0']")
    MR_SELECT    = (By.CSS_SELECTOR, "div div[id='react-select-3-option-0-1']")
    MRS_SELECT   = (By.CSS_SELECTOR, "div div[id='react-select-3-option-0-2']")
    MS_SELECT    = (By.CSS_SELECTOR, "div div[id='react-select-3-option-0-3']")
    PROF_SELECT  = (By.CSS_SELECTOR, "div div[id='react-select-3-option-0-4']")
    OTHER_SELECT = (By.CSS_SELECTOR, "div div[id='react-select-3-option-0-5']")


    # Old Style Select Menu
    OLD_STYLE_DROPDOWN_MENU = (By.CSS_SELECTOR, "div select[id='oldSelectMenu']")

    # Multiselect drop down menu
    MULTISELECT_MENU = (By.CSS_SELECTOR, "//*[@id='react-select-4-input']")
    GREEN = (By.CSS_SELECTOR, "div[id='react-select-13-option-0']")
    BLUE = (By.CSS_SELECTOR, "div[id='react-select-13-option-1']")
    BLACK = (By.CSS_SELECTOR, "div[id='react-select-13-option-2']")
    RED = (By.CSS_SELECTOR, "div[id='react-select-13-option-3']")
    REMOVE_ITEM_FROM_FIELD = (By.CSS_SELECTOR, "div svg[class='css-19bqh2r'] ")







    # DR_SELECT    = (By.CSS_SELECTOR, "div[class=' css-1hwfws3'] input[id='react-select-3-input']")
    # MR_SELECT    = (By.CSS_SELECTOR, "div[class=' css-1hwfws3'] input[id='react-select-3-input']")
    # MRS_SELECT   = (By.CSS_SELECTOR, "div[class=' css-1hwfws3'] input[id='react-select-3-input']")
    # MS_SELECT    = (By.CSS_SELECTOR, "div[class=' css-1hwfws3'] input[id='react-select-3-input']")
    # PROF_SELECT  = (By.CSS_SELECTOR, "div[class=' css-1hwfws3'] input[id='react-select-3-input']")
    # OTHER_SELECT = (By.CSS_SELECTOR, "div[class=' css-1hwfws3'] input[id='react-select-3-input']")









