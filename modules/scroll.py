import time
from selenium.webdriver.common.by import By


def scroll_page(driver, target_count=20, max_scrolls=20):

    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(max_scrolls):

        # Scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Count loaded profiles
        cards = driver.find_elements(By.XPATH, "//div[contains(@class,'entity-result')]")

        print(f"Scroll {i+1} → Profiles loaded: {len(cards)}")

        # Stop if enough profiles loaded
        if len(cards) >= target_count:
            print("Target profile count reached.")
            break

        # Stop if page can't scroll more
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            print("Reached end of page.")
            break

        last_height = new_height