import random
import time

def scroll_page(driver, scroll_count = 5, scroll_pause_time = 2):
    
    for i in range(scroll_count):
        
        #Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #Scrolls to the bottom of the page using JavaScript execution. This is necessary to load more content on LinkedIn pages that use infinite scrolling.
        time.sleep(scroll_pause_time + random.uniform(2, 4)) #Waits for a random amount of time between scrolls to mimic human behavior and avoid being detected as a bot. The pause time is randomized by adding a random value between 2 and 4 seconds to the base scroll_pause_time.
        
        print(f"SCrolled down {i + 1} time(s)")