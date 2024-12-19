from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    SAMPLE_PAGE_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    SAMPLE_FRAME_TEXT = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, "p")

class ModalDialogsPageLocators:
    SMALL_DIALOG_SHOW_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    LARGE_DIALOG_SHOW_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")

    SMALL_DIALOG_CLOSE = (By.CSS_SELECTOR, "button[id='closeSmallModal']")
    LARGE_DIALOG_CLOSE = (By.CSS_SELECTOR, "button[id='closeLargeModal']")

    BODY_SMALL_MODAL = (By.CSS_SELECTOR, "div[class ='modal-body']")
    BODY_LARGE_MODAL = (By.CSS_SELECTOR, "div[class ='modal-body'] p")

    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, "div[id ='example-modal-sizes-title-sm']")
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, "div[id ='example-modal-sizes-title-lg']")


