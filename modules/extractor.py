from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def result_extractor(driver):

    wait = WebDriverWait(driver, 15)

    # Wait until at least one result card loads
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'entity-result')]")
        )
    )

    profiles = driver.find_elements(By.XPATH, "//div[contains(@class,'entity-result')]")

    print("Profiles detected on page:", len(profiles))

    data = []
    seen_links = set()

    for profile in profiles:

        # ---------- GET PROFILE LINK + NAME ----------
        try:
            link_element = profile.find_element(
                By.XPATH,
                ".//a[contains(@href,'/in/')]"
            )

            link = link_element.get_attribute("href")

            if not link or link in seen_links:
                continue

            seen_links.add(link)

            name = link_element.text.strip()

            if not name:
                continue

        except:
            continue


        # ---------- GET TITLE (ROBUST METHOD) ----------
        title = "N/A"

        try:
            title_element = profile.find_element(
                By.XPATH,
                ".//div[contains(@class,'entity-result__primary-subtitle')]/span"
            )
            title = title_element.text.strip()

        except:
            pass


        # ---------- SAVE ----------
        data.append({
            "Name": name,
            "Title": title,
            "Profile Link": link
        })


    print("Unique profiles extracted:", len(data))
    return data