from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def result_extractor(driver):

    wait = WebDriverWait(driver, 10)

    # wait until results load
    wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'entity-result')]"))
    )

    
    profiles = driver.find_elements(By.XPATH, "//div[contains(@class,'entity-result')]")

    #profiles = driver.find_elements(By.XPATH, "//li[contains(@class,'reusable-search__result-container')]")

    print("Profiles found:", len(profiles))

    data = []

    for profile in profiles:

        try:
            name = profile.find_element(By.XPATH, ".//span[@aria-hidden='true']").text.strip()
        except:
            name = "N/A"

        try:
            title = profile.find_element(By.XPATH, ".//div[contains(@class,'t-14')]").text.strip()
        except:
            title = "N/A"

        try:
            link = profile.find_element(By.XPATH, ".//a[contains(@href,'/in/')]").get_attribute("href")
        except:
            link = "N/A"

        data.append({
            "Name": name,
            "Title": title,
            "Profile Link": link
        })

    return data
