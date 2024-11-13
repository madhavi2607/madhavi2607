from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up your Jira URL and login credentials
jira_url = 'https://id.atlassian.com/login?continue=https%3A%2F%2Fid.atlassian.com%2Fjoin%2Fuser-access%3Fresource%3Dari%253Acloud%253Ajira%253A%253Asite%252F42dba59f-cb48-493f-a34b-2bfd62ac3f65%26continue%3Dhttps%253A%252F%252Fcfainstitute.atlassian.net%252Fjira%252Fservicedesk%252Fprojects%252FITHD%252Fqueues&application=jira'  # Replace with your Jira URL
username = 'sdarji@cfainstitute.in'  # Replace with your username
api_token = 'sam'  # Replace with your API token

def login_to_jira():
    # Initialize WebDriver (change to your preferred browser)
    driver = webdriver.Chrome()

    # Open the Jira login page
    driver.get(jira_url)

    time.sleep(10)

    # # Wait for the login fields to load
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login-form-username')))

    # Enter username
    driver.find_element(By.ID, 'username').send_keys(username)

    time.sleep(5)
    driver.find_element(By.ID, 'login-submit').click()

    time.sleep(50)
    # Enter API token as password
    # driver.find_element(By.ID, 'login-submit').send_keys(api_token)

    # Click the login button
    # driver.find_element(By.ID, 'login').click()

    # # Wait for the dashboard to load
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'dashboard')))

    print("Logged in successfully.")

    # Close the browser if needed, or return the driver to continue working
    # driver.quit()

if __name__ == "__main__":
    login_to_jira()
