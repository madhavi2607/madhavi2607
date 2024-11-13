from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set Firefox options
options = Options()
# Uncomment the next line if you want to use a specific profile
# options.set_preference("profile", r"C:\Path\To\Your\Firefox\Profile")

# Initialize the WebDriver
driver = webdriver.Firefox(options=options)

# Navigate to the Jira URL
jira_url = 'https://cfainstitute.atlassian.net/jira/servicedesk/projects/ITHD/queues/custom/433'
driver.get(jira_url)

# Rest of your automation code...
time.sleep(50)