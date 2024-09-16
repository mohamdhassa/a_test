import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    # Set up Chrome options before initializing the WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Run headless for CI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # Maximize after initializing the driver

    yield driver  # This is returned to the tests

    driver.quit()  # Quit the driver after tests complete


def test_open_browser(driver):
    try:
        driver.get('wrong one')  # Intentional wrong URL for testing the exception
        print("First option started")
    except Exception as e:
        print(f"Second option started due to: {e}")
        driver.get("https://www.google.com/")
    time.sleep(2)


def test_open_google(driver):
    try:
        search_term = "selenium"
        search_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='APjFqb']"))
        )
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)
    except Exception as e:
        print(f"Error during search: {e}")
        time.sleep(2)


def test_open_first_result(driver):
    try:
        find_youtube = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3/span"))
        )
        find_youtube.click()
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
        find_youtube = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3"))
        )
        find_youtube.click()
        time.sleep(2)


def test_perfect_job(driver):
    try:
        print("Perfect job")
    except Exception as e:
        print(f"Something went wrong: {e}")


def test_search_selenium(driver):
    try:
        driver.get("https://www.google.com/")
        search = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='APjFqb']"))
        )
        search.send_keys("selenium")
        search.send_keys(Keys.RETURN)
        time.sleep(2)

        first_result = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3/span"))
        )
        first_result.click()
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")


def test_search_hello(driver):
    try:
        driver.get("https://www.google.com/")
        search = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='APjFqb']"))
        )
        search.send_keys("hello")
        search.send_keys(Keys.RETURN)
        time.sleep(2)

        first_result = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a/h3/span"))
        )
        first_result.click()
        time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        time.sleep(2)
        driver.quit()


def test_quit_browser(driver):
    driver.quit()
