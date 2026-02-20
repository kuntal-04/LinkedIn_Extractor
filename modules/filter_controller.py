from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_filter(driver, filter_name):

    wait = WebDriverWait(driver, 15)

    # wait until filter buttons appear
    buttons = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//button"))
    )

    for btn in buttons:
        text = btn.text.strip().lower()

        if filter_name.lower() in text:
            btn.click()
            print(f"{filter_name} filter selected.")
            return True

    print(f"{filter_name} filter not found.")
    return False
