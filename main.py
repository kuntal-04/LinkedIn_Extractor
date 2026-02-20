from modules.browser import start_browser       #Imports start_browser function from browser module. This function is responsible for launching the Chrome browser and navigating to LinkedIn homepage.
from modules.login import linkedin_login         #Imports linkedin_login function from login module. This function handles the process of logging into LinkedIn using provided email and password credentials.
from modules.secure_input import masked_input
from modules.search import linkedin_search
from modules.session import save_cookies, load_cookies



print("Starting LinkedIn Automation...")

#First ask for login credentials, then start browser.
email = input("Enter your LinkedIn email: ") #Prompts user to enter their LinkedIn email address and stores it in the variable 'email'.
password = masked_input("Enter your LinkedIn password: ") #Prompts user to enter their LinkedIn password securely (without echoing it to the terminal) and stores it in the variable 'password'.
keyword = input("Enter search keyword: ") #Prompts user to enter a search keyword for LinkedIn and stores it in the variable 'keyword'.

driver = start_browser()

#Try to load cookies and skip login if successful. If not, perform login and save cookies for next time.
logged_in = load_cookies(driver)
driver.refresh()

if not logged_in:
    linkedin_login(driver, email, password)       #Calls linkedin_login function with the browser driver and user credentials to perform the login process on LinkedIn.
    save_cookies(driver)
else:
    print("Session restored, already logged in!")

linkedin_search(driver, keyword)

input("Search completed, Press Enter to close browser.")
driver.quit() 
