from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def linkedin_login(driver, email, password):
    #Finds and clicks the "Sign in" button on LinkedIn homepage to navigate to login page.
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_button.click()
    
    time.sleep(2) #Waits for 2 seconds to allow login page to load. This is a simple way to ensure elements are available before interacting with them. In a more robust implementation, you might want to use WebDriverWait instead of sleep for better reliability.
    
    #Finds email input field, enters provided email, and simulates pressing Enter key to submit the form.
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)
    
    time.sleep(1) #Waits for 2 seconds to allow password field to load after submitting email.
    
    #Finds password input field, enters provided password, and simulates pressing Enter key to submit the form and complete login process.
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    time.sleep(5) #Waits for 5 seconds to allow login process to complete and LinkedIn homepage to load after successful login.
    