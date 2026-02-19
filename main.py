from modules.browser import start_browser       #Imports start_browser function from browser module. This function is responsible for launching the Chrome browser and navigating to LinkedIn homepage.
from modules.login import linkedin_login         #Imports linkedin_login function from login module. This function handles the process of logging into LinkedIn using provided email and password credentials.
print("Starting LinkedIn Automation...")
 
driver = start_browser()

email = input("Enter your LinkedIn email: ") #Prompts user to enter their LinkedIn email address and stores it in the variable 'email'.
password = input("Enter your LinkedIn password: ") #Prompts user to enter their LinkedIn password and stores it in the variable 'password'.

linkedin_login(driver, email, password) #Calls linkedin_login function with the browser driver and user credentials to perform the login process on LinkedIn.

input("Login process completed, Press Enter to close browser.")
driver.quit() 
