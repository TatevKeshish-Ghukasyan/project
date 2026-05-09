from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def get_weather(city="Yerevan"):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # без открытия браузера

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://www.google.com")

        search = driver.find_element(By.NAME, "q")
        search.send_keys(f"weather {city}")
        search.send_keys(Keys.RETURN)

        time.sleep(2)

        temp = driver.find_element(By.ID, "wob_tm").text
        desc = driver.find_element(By.ID, "wob_dc").text

        return f"{city}: {temp}°C, {desc}"

    except Exception as e:
        return f"Ошибка: {e}"

    finally:
        driver.quit()