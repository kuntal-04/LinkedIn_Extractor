from modules.browser import start_browser       #Imports start_browser function from browser module. This function is responsible for launching the Chrome browser and navigating to LinkedIn homepage.
from modules.login import linkedin_login         #Imports linkedin_login function from login module. This function handles the process of logging into LinkedIn using provided email and password credentials.
from modules.secure_input import masked_input
from modules.search import linkedin_search
from modules.session import save_cookies, load_cookies
from modules.scroll import scroll_page
from modules.extractor import result_extractor
from modules.exporter import export_data
import time


print("Starting LinkedIn Automation...")

#-----PHASE 1: User Login-----
#First ask for login credentials, then start browser.
email = input("Enter your LinkedIn email: ") #Prompts user to enter their LinkedIn email address and stores it in the variable 'email'.
password = masked_input("Enter your LinkedIn password: ") #Prompts user to enter their LinkedIn password securely (without echoing it to the terminal) and stores it in the variable 'password'.
keyword = input("Enter search keyword: ").replace("Search ", "").strip()
 #Prompts user to enter a search keyword for LinkedIn and stores it in the variable 'keyword'.
 #strip() removes any leading like 'search' from input and ensure the keyword is clean.

driver = start_browser()

#Try to load cookies and skip login if successful. If not, perform login and save cookies for next time.
logged_in = load_cookies(driver)
driver.refresh()

if not logged_in:
    linkedin_login(driver, email, password)       #Calls linkedin_login function with the browser driver and user credentials to perform the login process on LinkedIn.
    save_cookies(driver)
else:
    print("Session restored, already logged in!")

#-----PHASE 2: Searching and Scrolling results-----
time.sleep(3)
linkedin_search(driver, keyword)

# Force People results page directly
driver.get(f"https://www.linkedin.com/search/results/people/?keywords={keyword.replace(' ', '%20')}")

time.sleep(3)

scroll_page(driver, target_count = 25) #Scrolls the page to load more search results. The scroll_page function is called with the browser driver and a target count of 25 profiles to load.

print("Current URL:", driver.current_url)


#-----PHASE 3: Data Extraction-----
#Extracting data 
print("Extracting data from search...")
time.sleep(3)

data = result_extractor(driver)
print(f"\nTotal profiles found: {len(data)}\n")
for d in data:
    print(d)
    
#-----PHASE 4: Exporting Data-----
choice = input("Do you want to export the data? (y/n): ").lower()
choice = input("Enter export format (csv/excel/skip): ").lower()

if choice in ["csv", "excel"]:
    export_data(data, filetype=choice)
else:
    print("Export skipped.")

input("Automation done, Press Enter to close browser.")
driver.quit() 
