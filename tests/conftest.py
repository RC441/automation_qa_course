import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    # options = Options()
    # options.add_argument("--incognito")  # Режим инкогнито
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
