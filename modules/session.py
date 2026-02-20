import pickle   #Used to save python object in file. We used it to store cookies list.
import os

COOKIE_FILE = 'session/cookies.pkl'   #This is where login session will be stored.

def save_cookies(driver):
    os.makedirs("session", exist_ok=True)
    with open(COOKIE_FILE, "wb") as file:
        pickle.dump(driver.get_cookies(), file)   #write cookies to file so that next time we can reuse it.
        
def load_cookies(driver):
    if not os.path.exists(COOKIE_FILE):  #if cookies not stores=d, then log in requried.
        return False 
    
    with open(COOKIE_FILE, "rb") as file:
        cookies = pickle.load(file)     
        
    for cookie in cookies:
        driver.add_cookie(cookie)   #adds caved cookies back to the browser.
        
    return True
         