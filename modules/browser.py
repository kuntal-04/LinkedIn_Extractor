from selenium import webdriver
from selenium.webdriver.chrome.service import Service       #Service is a class from the Selenium library that allows you to manage the lifecycle of the ChromeDriver executable. It provides methods to start and stop the ChromeDriver service, which is necessary for running Selenium tests with the Chrome browser.
from webdriver_manager.chrome import ChromeDriverManager    #ChromeDriverManager is a library that automatically manages the ChromeDriver binary for Selenium. It ensures that you have the correct version of ChromeDriver installed and available for your Selenium tests, eliminating the need to manually download and configure the driver.

def start_browser():
    options = webdriver.ChromeOptions()                     #creates chrome configuration object 
    options.add_argument("--start-maximized")               #This line adds and arguement to the ChromeOptions object to start the browser in maximized mode when launched. This means that when the browser window opens, it will automatically be maximized to fill the entire screen, providing a better user experience and allowing for more content to be visible.
    
    driver = webdriver.Chrome(                              #Creates new browser instance using Chrome webdriver.
        service=Service(ChromeDriverManager().install()),   #1. ChromeDriverManager downloads driver and returns path to it. 2. Service class is used to manage the lifecycle of the ChromeDriver executable. 3. Selenium connects to the ChromeDriver using provided path.
        options=options)
    
    driver.get("https://linkedin.com")                      #Opens LinkedIn homepage in the browser. Without this, browser will open blank page.
    return driver                                           #Returns browser controller object to main program.
