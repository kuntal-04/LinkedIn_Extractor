from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def linkedin_search(driver, keyword):
    
    wait = WebDriverWait(driver, 15) #Creates WebDriverWait object with a timeout of 15 seconds. This will be used to wait for certain elements to become available on the page before interacting with them, improving reliability of the script.
    
    search_bar = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@placeholder, 'Search')]"))
    )        #Finds search bar element on LinkedIn page using XPath selector that looks for an input field with a placeholder attribute containing the word "Search".
    
    search_bar.clear() #Clears any existing text in the search bar to ensure that only the new keyword is entered.
    search_bar.send_keys(keyword) #Enters the provided keyword into the search bar.
    search_bar.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
    