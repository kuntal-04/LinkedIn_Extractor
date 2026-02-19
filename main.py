from modules.browser import start_browser       #Imports start_browser function from browser module. This function is responsible for launching the Chrome browser and navigating to LinkedIn homepage.
from modules.login import linkedin_login         #Imports linkedin_login function from login module. This function handles the process of logging into LinkedIn using provided email and password credentials.
from modules.secure_input import masked_input

print("Starting LinkedIn Automation...")

#First ask for login credentials, then start browser.
email = input("Enter your LinkedIn email: ") #Prompts user to enter their LinkedIn email address and stores it in the variable 'email'.
password = masked_input("Enter your LinkedIn password: ") #Prompts user to enter their LinkedIn password securely (without echoing it to the terminal) and stores it in the variable 'password'.
 
driver = start_browser()

linkedin_login(driver, email, password) #Calls linkedin_login function with the browser driver and user credentials to perform the login process on LinkedIn.

input("Login process completed, Press Enter to close browser.")
driver.quit() 
