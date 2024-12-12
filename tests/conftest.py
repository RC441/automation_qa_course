import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():

    # MODDED OT ADD ADBLOCK
    # Настройка пути к профилю
    chrome_options = Options()
    path = "--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data"
    chrome_options.add_argument(path)  # Укажите путь к папке профиля
    chrome_options.add_argument("--profile-directory=Profile 3")  # Название профиля (например, "Default")
    # chrome_options.add_argument("--profile-directory=Default")
    # chrome_options.add_argument("--headless=new")  # Для запуска без GUI
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()









    # # ORIG
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # yield driver
    # driver.quit()

    # DIFFERENT OPTIONS
    # options.add_argument("--incognito")  # Режим инкогнито
    # chrome_options.add_argument("--profile-directory=Default")
    # chrome_options.add_argument("--headless=new")  # Для запуска без GUI
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-dev-shm-usage")